from .transcription.aws_transcription_service import AwsTranscriptionService
from .transcription.ibm_transcription_service import IbmTranscriptionService
from .transcription.contract import TranscriptionContract
from .core.service_contract import ServiceContract
from ..common.constants import SupportedVendors, SupportedServices


class ServiceFactory(object):
    """
    A factory for various services.
    """

    @classmethod
    def get_transcription_service(cls, vendor) -> TranscriptionContract:
        """
        Returns the transcription service impl as per vendor, raises error if impl can not be resolved.
        :param vendor: name of vendor. See supported vendor in constants.
        :return: TranscriptionContract
        """
        transcription_service = None
        if vendor == SupportedVendors.Amazon.value:
            transcription_service = AwsTranscriptionService()
        if vendor == SupportedVendors.Ibm.value:
            transcription_service = IbmTranscriptionService()
        return transcription_service

    @classmethod
    def get_service(cls, service, vendor) -> ServiceContract:
        """
        Returns the service contract implementation based on service name and vendor name, otherwise raises Exception.
        :param service:
        :param vendor:
        :return:
        """
        service_obj = None
        if not service:
            raise Exception('Illegal argument: service')
        if not vendor:
            raise Exception('Illegal argument: vendor')
        if service == SupportedServices.TranscriptionService.value:
            service_obj = cls.get_transcription_service(vendor)
        return service_obj
