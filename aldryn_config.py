# -*- coding: utf-8 -*-
from aldryn_client import forms


class Form(forms.BaseForm):
    ga_view_id = forms.CharField(
        'Google Analytics View ID',
        required=True,
    )

    def to_settings(self, data, settings):
        settings['INSTALLED_APPS'].extend([
            'wagtailfontawesome',
        ])

        settings['GA_VIEW_ID'] = data['ga_view_id']

        return settings
