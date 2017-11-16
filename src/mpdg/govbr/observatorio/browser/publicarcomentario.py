# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from Products.statusmessages.interfaces import IStatusMessage
from plone import api


grok.templatedir('templates')


class PublicarComentario(grok.View):
    grok.name('publicar_comentario')
    grok.require('cmf.ModifyPortalContent')
    grok.context(Interface)

    def update(self):
        uids    = self.request.form.get('uids')
        catalog = api.portal.get_tool('portal_catalog')
        brains  = catalog.searchResults(UID=uids)
        if brains:
            obj = brains[0].getObject()
            api.content.transition(obj=obj, transition='publish')
            return self._back_to(obj.aq_parent, 'Comentário publicado com sucesso!')
        else:
            return self._back_to(self.context.aq_parent, 'Não foi encontrado um comentário com esse UID')

    def _back_to(self, context, message=None):

        target = context.absolute_url()+'/@@manage-comments-view'

        if message:
            messages = IStatusMessage(self.request)
            messages.add(message, type='info')

        return self.request.response.redirect(target)

    def message(self, mensagem):
        messages = IStatusMessage(self.request)
        messages.add(mensagem, type='info')
        return
