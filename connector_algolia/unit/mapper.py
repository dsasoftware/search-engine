# -*- coding: utf-8 -*-
# © 2016 Akretion (http://www.akretion.com)
# Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp import models
from openerp.addons.connector_search_engine.unit.mapper import JsonExportMapper
from ..backend import algolia


@algolia
class JsonExportMapper(JsonExportMapper):

    def _apply(self, map_record, options=None):
        res = super(JsonExportMapper, self)._apply(map_record, options=None)
        exporter = self.connector_env.index_record.exporter_id
        object_id = map_record._source[self.connector_env.index_record.id_key]
        if isinstance(object_id, models.Model):
            res['objectID'] = object_id.id
        else:
            res['objectID'] = object_id
        return res
