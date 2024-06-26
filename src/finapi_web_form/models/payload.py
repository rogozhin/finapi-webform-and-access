# coding: utf-8

"""
    finAPI Web Form 2.0

    The following pages give you some general information on how to use our APIs.<br/>The actual API services documentation then follows further below. You can use the menu to jump between API sections.<br/><br/>This page has a built-in HTTP(S) client, so you can test the services directly from within this page, by filling in the request parameters and/or body in the respective services, and then hitting the TRY button. Note that you need to be authorized to make a successful API call. To authorize, refer to the '<a target='_blank' href='https://docs.finapi.io/?product=access#tag--Authorization'>Authorization</a>' section of Access, or in case you already have a valid user token, just use the QUICK AUTH on the left.<br/>Please also remember that all user management functions should be looked up in <a target='_blank' href='https://docs.finapi.io/?product=access'>Access</a>.<br/><br/>You should also check out the <a target='_blank' href='https://documentation.finapi.io/webform/'>Web Form 2.0 Public Documentation</a> as well as <a target='_blank' href='https://documentation.finapi.io/access/'>Access Public Documentation</a> for more information. If you need any help with the API, contact <a href='mailto:support@finapi.io'>support@finapi.io</a>.<br/><h2 id=\"general-information\">General information</h2><h3 id=\"general-request-ids\"><strong>Request IDs</strong></h3>With any API call, you can pass a request ID via a header with name \"X-Request-Id\". The request ID can be an arbitrary string with up to 255 characters. Passing a longer string will result in an error.<br/><br/>If you don't pass a request ID for a call, finAPI will generate a random ID internally.<br/><br/>The request ID is always returned back in the response of a service, as a header with name \"X-Request-Id\".<br/><br/>We highly recommend to always pass a (preferably unique) request ID, and include it into your client application logs whenever you make a request or receive a response(especially in the case of an error response). finAPI is also logging request IDs on its end. Having a request ID can help the finAPI support team to work more efficiently and solve tickets faster.<h3 id=\"type-coercion\"><strong>Type Coercion</strong></h3>In order to ease the integration for some languages, which do not natively support high precision number representations, Web Form 2.0 API supports relax type binding for the openAPI type <code>number</code>, which is used for money amount fields. If you use one of those languages, to avoid precision errors that can appear from <code>float</code> values, you can pass the amount as a <code>string</code>.<h3 id=\"general-faq\"><strong>FAQ</strong></h3><strong>Is there a finAPI SDK?</strong><br/>Currently we do not offer a native SDK, but there is the option to generate an SDKfor almost any target language via OpenAPI. Use the 'Download SDK' button on this page for SDK generation.<br/><br/><strong>Why do I need to keep authorizing when calling services on this page?</strong><br/>This page is a \"one-page-app\". Reloading the page resets the OAuth authorization context. There is generally no need to reload the page, so just don't do it and your authorization will persist.

    The version of the OpenAPI document: 2.709.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Payload(BaseModel):
    """
    Payload of the web form
    """ # noqa: E501
    bank_connection_id: Optional[StrictInt] = Field(default=None, description="Identifier of the bank connection in the Access API. Initialized as soon as the Web Form reaches a final status and a bank connection exists in Access. Use this ID to gather Bank Connection data from Access endpoints like, \"<a target='_blank' href='https://docs.finapi.io/?product=access#get-/api/v1/bankConnections/-id-'>Get a bank connection</a>\" or \"<a target='_blank' href='https://docs.finapi.io/?product=access#get-/api/v1/accounts'>Get and search all accounts</a>\".<br/>This field is mutually exclusive with <code>paymentId</code> and <code>standingOrderId</code>.", alias="bankConnectionId")
    payment_id: Optional[StrictInt] = Field(default=None, description="Identifier of the payment in the Access API. Initialized as soon as the Web Form reaches a final status and a payment exists in Access. Use this ID to get Payment initialization data from the Access endpoint, \"<a target='_blank' href='https://docs.finapi.io/?product=access#get-/api/v1/payments'>Get payments</a>\".<br/>This field is mutually exclusive with <code>bankConnectionId</code> and <code>standingOrderId</code>.", alias="paymentId")
    standing_order_id: Optional[StrictInt] = Field(default=None, description="Identifier of the standing order in the Access API. Initialized as soon as the Web Form reaches a final status and a standing order exists in Access. Use this ID to get Standing Order initialization data from the Access endpoint, \"<a target='_blank' href='https://docs.finapi.io/?product=access#get-/api/v1/standingOrders'>Get standing orders</a>\".<br/>This field is mutually exclusive with <code>bankConnectionId</code> and <code>paymentId</code>.", alias="standingOrderId")
    error_code: Optional[StrictStr] = Field(default=None, description="Reason of the web form failure.<br/><strong>NOTE:</strong> This enum can be extended in the future as new cases arise!<br/><br/>Codes can be interpreted as follows:<br/>&bull; <code>ENTITY_EXISTS</code> - Access API rejected the import because of detected bank connection duplication;<br/>&bull; <code>BANK_SERVER_REJECTION</code> - the flow has been terminated on the bank side, e.g., in case of incorrect credentials;<br/>&bull; <code>INTERRUPTED</code> - web form has been reloaded or re-opened on a step where it's not supported;<br/>&bull; <code>INVALID_TOKEN</code> - the given access token expired or became invalid during the flow; <br/>&bull; <code>MANDATOR_MISCONFIGURATION</code> - the mandator is not properly configured on the Access side, e.g., it is still configured to use the old web form, or the scraper interface has been selected by the Web Form 2.0 but using it is not allowed on the mandator level. Please contact our support team (<a href='mailto:support@finapi.io'>support@finapi.io</a>) for troubleshooting;<br/>&bull; <code>NO_ACCOUNTS_FOR_TYPE_LIST</code> - in the end of the web form flow there were no accounts of type requested in the API call; <br/>&bull; <code>UNDETERMINED_BANK</code> - the given search criteria resulted in either zero or multiple bank entries;<br/>&bull; <code>UNEXPECTED_ACCESS_RESPONSE</code> - an unexpected response has been received from the Access API - similarly to the <code>INTERNAL_ERROR</code> code, please forward all details to our Customer Support team; <br/>&bull; <code>UNSUPPORTED_FEATURE</code> - Access API rejected the request because the requested feature is not supported, e.g., a payment with the execution date in the future was requested for a bank that does not support it;<br/>&bull; <code>UNSUPPORTED_ORDER</code> - Access API rejected the payment request because the associated account does not have the required capabilities;<br/>&bull; <code>INTERNAL_ERROR</code> - the reason of the failure can not be identified - please forward all the details to our Customer Support team in order to get more info and also help us to eliminate the issue.", alias="errorCode")
    error_message: Optional[StrictStr] = Field(default=None, description="Details of web form failure.", alias="errorMessage")
    __properties: ClassVar[List[str]] = ["bankConnectionId", "paymentId", "standingOrderId", "errorCode", "errorMessage"]

    @field_validator('error_code')
    def error_code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ENTITY_EXISTS', 'BANK_SERVER_REJECTION', 'INTERNAL_ERROR', 'INTERRUPTED', 'INVALID_TOKEN', 'MANDATOR_MISCONFIGURATION', 'NO_ACCOUNTS_FOR_TYPE_LIST', 'UNDETERMINED_BANK', 'UNEXPECTED_ACCESS_RESPONSE', 'UNSUPPORTED_FEATURE', 'UNSUPPORTED_ORDER']):
            raise ValueError("must be one of enum values ('ENTITY_EXISTS', 'BANK_SERVER_REJECTION', 'INTERNAL_ERROR', 'INTERRUPTED', 'INVALID_TOKEN', 'MANDATOR_MISCONFIGURATION', 'NO_ACCOUNTS_FOR_TYPE_LIST', 'UNDETERMINED_BANK', 'UNEXPECTED_ACCESS_RESPONSE', 'UNSUPPORTED_FEATURE', 'UNSUPPORTED_ORDER')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Payload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if bank_connection_id (nullable) is None
        # and model_fields_set contains the field
        if self.bank_connection_id is None and "bank_connection_id" in self.model_fields_set:
            _dict['bankConnectionId'] = None

        # set to None if payment_id (nullable) is None
        # and model_fields_set contains the field
        if self.payment_id is None and "payment_id" in self.model_fields_set:
            _dict['paymentId'] = None

        # set to None if standing_order_id (nullable) is None
        # and model_fields_set contains the field
        if self.standing_order_id is None and "standing_order_id" in self.model_fields_set:
            _dict['standingOrderId'] = None

        # set to None if error_code (nullable) is None
        # and model_fields_set contains the field
        if self.error_code is None and "error_code" in self.model_fields_set:
            _dict['errorCode'] = None

        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict['errorMessage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Payload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bankConnectionId": obj.get("bankConnectionId"),
            "paymentId": obj.get("paymentId"),
            "standingOrderId": obj.get("standingOrderId"),
            "errorCode": obj.get("errorCode"),
            "errorMessage": obj.get("errorMessage")
        })
        return _obj


