# -*- coding: utf-8 -*-
from zope import schema
from five import grok
from Products.CMFCore.interfaces import ISiteRoot
from plone.z3cform import layout
from plone.directives import form
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.autoform import directives
from mpdg.govbr.observatorio.config import (
    EMAIL_OBS_ASSINATURA,
    EMAIL_OBS_ADMIN,
    EMAIL_PRATICA_APROVADA,
    EMAIL_COMENTARIO_ADMIN,
    EMAIL_COMENTARIO_APROVADO,
    EMAIL_COMENTARIO_REPROVADO
)


class IObservatorio_email(form.Schema):

    adm_observatorio = schema.TextLine(
        title = u'Email do Administrador do Observatório',
        description = u'Informe o email do Administrador do Observatório',
        required = True,
        default = u'catia.parreira@planejamento.gov.br',
    )

    directives.widget(enviar_email_assinatura='plone.app.z3cform.wysiwyg.WysiwygFieldWidget')
    enviar_email_assinatura=schema.Text(
        title=u'Mensagem de Assinatura',
        description=u'Informe a assinatura de email. Será exibida no final da mensagem ',
        required=True,
        default =EMAIL_OBS_ASSINATURA
    )

    directives.widget(enviar_email_adm='plone.app.z3cform.wysiwyg.WysiwygFieldWidget')
    enviar_email_adm=schema.Text(
        title=u'Notificação de nova prática',
        description=u"""Informe a mensagem que o administrador irá receber no email após o usuário escrever uma boa prática pelo Observatório.
        Variáveis: [nome_pratica], [url_pratica], [descricao_pratica].""",
        required=True,
        default=EMAIL_OBS_ADMIN

    )

    directives.widget(pratica_aprovada='plone.app.z3cform.wysiwyg.WysiwygFieldWidget')
    pratica_aprovada=schema.Text(
        title=u'Prática aprovada',
        description=u"""Informe a mensagem que o usuário irá receber quando a prática for aprovada
        Variáveis: [nome_pratica], [descricao_pratica], [url_pratica]""",
        required=True,
        default=EMAIL_PRATICA_APROVADA

    )

    directives.widget(comentario_info_admin='plone.app.z3cform.wysiwyg.WysiwygFieldWidget')
    comentario_info_admin=schema.Text(
        title=u'Notificação de novo comentário ',
        description=u"""Informe a mensagem que o administrador irá receber no email após o usuário escrever um comentário pelo Observatório.
        Variáveis: [url_aprovacao].""",
        required=True,
        default=EMAIL_COMENTARIO_ADMIN
    )

    directives.widget(comentario_aprovado='plone.app.z3cform.wysiwyg.WysiwygFieldWidget')
    comentario_aprovado=schema.Text(
        title=u'Comentário Aprovado',
        description=u"""Informe a mensagem que o usuário irá receber quando o comentário for aprovado
        Variáveis: [url_pratica]""",
        required=True,
        default=EMAIL_COMENTARIO_APROVADO

    )

    directives.widget(comentario_reprovado='plone.app.z3cform.wysiwyg.WysiwygFieldWidget')
    comentario_reprovado=schema.Text(
        title=u'Comentário Reprovado',
        description=u"""Informe a assinatura que o usuário irá receber se o comentário for reprovado.
        Variáveis: [url_pratica]""",
        required=True,
        default=EMAIL_COMENTARIO_REPROVADO
    )


class ObservatorioSettings(RegistryEditForm):
    """
    """
    schema = IObservatorio_email
    label = u"Configurações do Observatório"


class SettingsView(grok.View):
    """
    """
    grok.name("observatorio-adm")
    grok.context(ISiteRoot)
    grok.require('cmf.ManagePortal')

    def render(self):
        view_factor = layout.wrap_form(ObservatorioSettings, ControlPanelFormWrapper)
        view = view_factor(self.context, self.request)
        return view()
