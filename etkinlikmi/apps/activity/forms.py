# Django
from django import forms
from django.conf import settings
from django.utils.html import format_html
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

# Local Django
from activity.extension import UPLOAD_DOCUMENT_TYPE

class ActivityDocumentAdminForm(forms.ModelForm):
    document = forms.FileField(label=_('Document'))

    def clean_document(self):
         document = self.cleaned_data['document']

         if 'document' in self.changed_data:

             if not document.content_type in UPLOAD_DOCUMENT_TYPE:
                 raise forms.ValidationError(
                    _('Please only upload document (doc, pdf, txt, exel, powerpoint).')
                )

             if document._size > settings.MAX_UPLOAD_SIZE:
                   raise ValidationError(_('Please keep filesize under (1MB).'))
         return document
