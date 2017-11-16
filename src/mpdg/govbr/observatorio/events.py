# -*- coding: utf-8 -*-
from plone import api
from five import grok
import json
from mpdg.govbr.observatorio.mailer import simple_send_mail
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from Products.CMFCore.interfaces import IActionSucceededEvent
from mpdg.govbr.observatorio.content.interfaces import IComentario
from zope.lifecycleevent.interfaces import IObjectRemovedEvent
from mpdg.govbr.observatorio.browser.utils import get_observatorio_config, transform_message


def send_email_after_approvation(context, event):
    wf = api.portal.get_tool('portal_workflow')
    history = wf.getHistoryOf('simple_publication_workflow', context)
    status = history[-1]
    if status['review_state'] == 'published':
        nome_do_usuario = context.Creator()
        usuario = api.user.get(username=nome_do_usuario)
        email = usuario.getProperty('email')
        portal_site = api.portal.get()
        titulo_do_site = portal_site.getProperty('title_2')
        descricao_pratica = context.Description()
        url_pratica =context.absolute_url()
        url_fale ="/fale-conosco/@@fale-conosco"
        nome_pratica = context.Title()
        send_email_users(nome_pratica,descricao_pratica,url_pratica, email, titulo_do_site,
            get_observatorio_config('pratica_aprovada') )


def send_email_users(nome_pratica,descricao_pratica ,url_pratica,email,titulo_do_site,message):
    """enviar um email para o usuario informando que a pratica foi aprovada"""
    assinatura_email = get_observatorio_config('enviar_email_assinatura')
    finalmessage = transform_message(text=message, nome_pratica=nome_pratica, descricao_pratica=descricao_pratica,
                                    url_pratica=url_pratica )
    msg_final =finalmessage + '\n' + assinatura_email

    address ='%s' % (email)
    subject ='Sua Prática no %s foi aprovada' %(titulo_do_site)

    return simple_send_mail(msg_final,address,subject)


def get_pratica_url(context):
    pratica = context.aq_parent
    return pratica.absolute_url()


def notify_admin_new_comment(context, event):
    """notifica o administrador do observatorio que ha novo comentario pendente de aprovacao"""
    url_aprovacao = '{0}/@@manage-comments-view'.format(get_pratica_url(context))

    registry = getUtility(IRegistry)
    text=get_observatorio_config('comentario_info_admin')

    message=transform_message(text=text, url_aprovacao=url_aprovacao)

    address = get_observatorio_config('adm_observatorio')
    subject = 'Novo comentário pendente na prática %s' %(context.Title())

    return simple_send_mail(message,address,subject)


@grok.subscribe(IComentario, IActionSucceededEvent)
def notify_user_comment_published(context, event):
    """notifica o usuario que seu comentario foi publicado"""
    if event.action == 'publish':
        url_pratica = get_pratica_url(context)

        assinatura = get_observatorio_config('enviar_email_assinatura')
        text = get_observatorio_config('comentario_aprovado')

        # transformar as variaveis de texto em valores dinamicos
        message = transform_message(text=text,url_pratica=url_pratica)
        menssagem_final = message + '\n' + assinatura
        address = context.getEmail()

        subject = 'Seu comentário foi aprovado'

        return simple_send_mail(menssagem_final,address,subject)
