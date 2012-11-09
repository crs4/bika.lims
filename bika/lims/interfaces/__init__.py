from plone.theme.interfaces import IDefaultPloneLayer
from zope.interface import Interface

class IBikaLIMS(Interface):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "bika" theme, this interface must be its layer
    """

class IClientFolder(Interface):
    """Client folder"""

class IClient(Interface):
    """Client"""

class IBatchFolder(Interface):
    """Batch folder"""

class IBatch(Interface):
    """Batch"""
    
class IBatchLabels(Interface):
    """Batch label"""

class IAnalysisRequest(Interface):
    """Analysis Request"""

class IAnalysisRequestsFolder(Interface):
    """AnalysisRequests Folder"""

class IAnalysis(Interface):
    """Analysis"""

class IDuplicateAnalysis(Interface):
    """DuplicateAnalysis"""

class IQueries(Interface):
    """Query interface """

class IReferenceAnalysis(Interface):
    """Reference Analyses """

class IReportFolder(Interface):
    """Report folder"""

class ISample(Interface):
    """Sample"""

class ISampleMatrix(Interface):
    """Sample Matrix"""

class ISampleMatrices(Interface):
    """Sample Matrices"""

class ISamplePartition(Interface):
    """Sample"""

class ISamplesFolder(Interface):
    """Samples Folder"""

class ISamplingDeviation(Interface):
    """Sampling Deviation"""

class ISamplingDeviations(Interface):
    """Sampling Deviations"""

class IWorksheetFolder(Interface):
    """WorksheetFolder"""

class IWorksheet(Interface):
    """Worksheet"""

class IReferenceSample(Interface):
    """Reference Sample"""

class IReferenceSamplesFolder(Interface):
    """Reference Samples Folder"""

class IReferenceSupplier(Interface):
    """Reference Supplier"""

class IReferenceSuppliers(Interface):
    """Reference Suppliers """

class IReportsFolder(Interface):
    """Reports Folder"""

class IInvoice(Interface):
    """Invoice"""

class IInvoiceBatch(Interface):
    """Invoice Batch"""

class IInvoiceFolder(Interface):
    """Invoices Folder"""

class IHaveNoBreadCrumbs(Interface):
    """Items which do not display breadcrumbs"""

class IIdServer(Interface):
    """ Interface for ID server """
    def generate_id(self, portal_type, batch_size = None):
        """ Generate a new id for 'portal_type' """

class IBikaSetup(Interface):
    ""

class IAnalysisCategory(Interface):
    ""
class IAnalysisCategories(Interface):
    ""
class IAnalysisService(Interface):
    ""
class IAnalysisServices(Interface):
    ""
class IAttachmentTypes(Interface):
    ""
class ICalculation(Interface):
    ""
class ICalculations(Interface):
    ""
class IContacts(Interface):
    ""
class IContact(Interface):
    ""
class IDepartments(Interface):
    ""
class IContainers(Interface):
    ""
class IContainerTypes(Interface):
    ""
class IInstruments(Interface):
    ""
class IAnalysisSpecs(Interface):
    ""
class IAnalysisProfiles(Interface):
    ""
class IARTemplates(Interface):
    ""
class ILabContacts(Interface):
    ""
class ILabContact(Interface):
    ""
class IMethods(Interface):
    ""
class ILabProducts(Interface):
    ""
class ISampleOrigins(Interface):
    ""
class ISamplePoints(Interface):
    ""
class ISampleTypes(Interface):
    ""
class IPatients(Interface):
    ""
class IPatient(Interface):
    ""
class IPreservations(Interface):
    ""
class IDoctors(Interface):
    ""
class IDoctor(Interface):
    ""
class IDrugs(Interface):
    ""
class IDrugProhibitions(Interface):
    ""
class IImmunizations(Interface):
    ""
class IReferenceManufacturers(Interface):
    ""
class IReferenceDefinitions(Interface):
    ""
class ISymptoms(Interface):
    ""
class IDiseases(Interface):
    ""
class IAetiologicAgents(Interface):
    ""
class ITreatments(Interface):
    ""
class IVaccinationCenter(Interface):
    ""
class IVaccinationCenters(Interface):
    ""
class ICaseStatuses(Interface):
    ""
class ICaseOutcomes(Interface):
    ""
class IWorksheetTemplates(Interface):
    ""

class IBikaCatalog(Interface):
    ""
class IBikaSetupCatalog(Interface):
    ""
