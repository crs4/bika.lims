from AccessControl import ClassSecurityInfo
from Products.Archetypes.Registry import registerWidget
from Products.Archetypes.Widget import TypesWidget
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from bika.lims import PMF, bikaMessageFactory as _
from bika.lims.browser import BrowserView
from bika.lims.browser.bika_listing import BikaListingView
from bika.lims.idserver import renameAfterCreation
from bika.lims.permissions import *
from operator import itemgetter
import json
import plone


class CaseAetiologicAgentsView(BrowserView):
    template = ViewPageTemplateFile("case_aetiologicagents.pt")

    def __init__(self, context, request, fieldvalue, allow_edit):
        self.context = context
        self.request = request
        self.fieldvalue = fieldvalue
        self.allow_edit = allow_edit

    def __call__(self):
        return self.template()
    
    def hasAetiologicAgents(self):
        return len(self.context.getAetiologicAgents())>0
    

class CaseAetiologicAgentsWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro': "bika_widgets/caseaetiologicagentswidget",
        'helper_js': ("bika_widgets/caseaetiologicagentswidget.js",),
        'helper_css': ("bika_widgets/caseaetiologicagentswidget.css",),
    })

    security = ClassSecurityInfo()

    security.declarePublic('process_form')

    def process_form(self, instance, field, form, empty_marker=None, emptyReturnsMarker=False):
        """ Return a list of dictionaries fit for Aetiologic agents RecordsField
        """
        value = len(instance.getAetiologicAgents())>0 and instance.getAetiologicAgents() or []
        if 'CAE_clear' in form:
            value = []
            
        elif 'CAE_delete' in form:
            valueout = []
            for i in range(len(value)):
                if not ('CAE_SelectItem-%s'%i in form):
                    valueout.append(value[i])
            value = valueout
            
        elif 'CAE_submitted' in form:
            bsc = getToolByName(instance, 'bika_setup_catalog')
            for i in range(len(form.get('CAE_Title', []))):
                T = form['CAE_Title'][i]
                D = form['CAE_Description'][i]
                S = form['CAE_Subtype'][i]

                # Create new Aetiologic Agent entry if none exists
                list = bsc(portal_type='AetiologicAgent', title=T)
                #if not list:
                #    folder = instance.bika_setup.bika_aetiologicagents
                #    _id = folder.invokeFactory('AetiologicAgent', id='tmp')
                #    obj = folder[_id]
                #    obj.edit(title=T, description=D)
                #    if S and len(S) > 0:
                #        prova='hola'
                #    obj.unmarkCreationFlag()
                #    renameAfterCreation(obj)
                value.append({'Title': T, 'Description': D, 'Subtype': S})
        return value, {}

    security.declarePublic('CaseAetiologicAgents')

    def CaseAetiologicAgents(self, field, allow_edit=False):
        """ Prints a bika listing with current case aetiologic agents
            field contains the archetypes field (list of dict)
        """
        fieldvalue = getattr(field, field.accessor)()
        view = CaseAetiologicAgentsView(self,
                                self.REQUEST,
                                fieldvalue=fieldvalue,
                                allow_edit=allow_edit)
        return view()

registerWidget(CaseAetiologicAgentsWidget,
               title='Aetiologic agents',
               description="Laboratory confirmed aetiologic agent and subtype, as the disease's cause",
               )