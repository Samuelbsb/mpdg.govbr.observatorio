# -*- coding: utf-8 -*-

PROJECTNAME = "mpdg.govbr.observatorio"


ADD_PERMISSIONS = {

    'BoaPratica': 'mpdg.govbr.observatorio: Add BoaPratica',
    'Comentario': 'mpdg.govbr.observatorio: Add Comentario',
    'Contador': 'mpdg.govbr.observatorio: Add Contador'
    }

EMAIL_OBS_ASSINATURA =u'<p>Atenciosamente,</p>'\
                      u'<p>Equipe do Governo Digital.</p>'


EMAIL_OBS_ADMIN = u'<p>Há uma nova prática para análise de aprovação.</p>' \
                  u'<p>Clique no link para visualizar a boa prática: [url_pratica] </p>'



EMAIL_PRATICA_APROVADA = u'<p>A prática: [nome_pratica] foi aprovada </p>' \
                        u'<p> Descrição: [descricao_pratica] </p>' \
                        u'<p>Link de visualização da prática: [url_pratica] </p>'



EMAIL_COMENTARIO_ADMIN =u'<p>Há um novo comentário para análise de aprovação.</p>'\
                        u'<p>Clique no link para visualizar a boa prática: [url_aprovacao] </p>'



EMAIL_COMENTARIO_APROVADO = u'<p>Seu comentário foi aprovado </p>'\
                            u'</p>link para visualizar a prática: [url_pratica] </p>'




EMAIL_COMENTARIO_REPROVADO =u'<p>Seu comentário foi rejeitado pois fere as políticas de uso do sítio/Política de Privacidade </p>' \
                            u'<p>Clique no link para visualizar a prática: [url_pratica] </p> '
