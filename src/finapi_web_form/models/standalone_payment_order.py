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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from finapi_web_form.models.amount import Amount
from finapi_web_form.models.standalone_payment_recipient import StandalonePaymentRecipient
from typing import Optional, Set
from typing_extensions import Self

class StandalonePaymentOrder(BaseModel):
    """
    Payment order
    """ # noqa: E501
    recipient: StandalonePaymentRecipient
    structured_remittance_information: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="This attribute is used to submit structured remittance information for the domestic payments. Please refer to the documentation for more details. For more information, please check the <a href=\"https://documentation.finapi.io/payments/ Czech-Republic-Domestic-Transfers.3045916711.html\">FAQ article</a>. ", alias="structuredRemittanceInformation")
    amount: Amount
    purpose: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=2000)]] = Field(default=None, description="The purpose of the transfer transaction")
    sepa_purpose_code: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="SEPA purpose code, according to ISO 20022, external codes set.<br/>Please note that the SEPA purpose code may be ignored by some banks.", alias="sepaPurposeCode")
    end_to_end_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=35)]] = Field(default=None, description="End-To-End ID for the transfer transaction.", alias="endToEndId")
    __properties: ClassVar[List[str]] = ["recipient", "structuredRemittanceInformation", "amount", "purpose", "sepaPurposeCode", "endToEndId"]

    @field_validator('sepa_purpose_code')
    def sepa_purpose_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9]{4}$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9]{4}$/")
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
        """Create an instance of StandalonePaymentOrder from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recipient
        if self.recipient:
            _dict['recipient'] = self.recipient.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        # set to None if structured_remittance_information (nullable) is None
        # and model_fields_set contains the field
        if self.structured_remittance_information is None and "structured_remittance_information" in self.model_fields_set:
            _dict['structuredRemittanceInformation'] = None

        # set to None if purpose (nullable) is None
        # and model_fields_set contains the field
        if self.purpose is None and "purpose" in self.model_fields_set:
            _dict['purpose'] = None

        # set to None if sepa_purpose_code (nullable) is None
        # and model_fields_set contains the field
        if self.sepa_purpose_code is None and "sepa_purpose_code" in self.model_fields_set:
            _dict['sepaPurposeCode'] = None

        # set to None if end_to_end_id (nullable) is None
        # and model_fields_set contains the field
        if self.end_to_end_id is None and "end_to_end_id" in self.model_fields_set:
            _dict['endToEndId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StandalonePaymentOrder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "recipient": StandalonePaymentRecipient.from_dict(obj["recipient"]) if obj.get("recipient") is not None else None,
            "structuredRemittanceInformation": obj.get("structuredRemittanceInformation"),
            "amount": Amount.from_dict(obj["amount"]) if obj.get("amount") is not None else None,
            "purpose": obj.get("purpose"),
            "sepaPurposeCode": obj.get("sepaPurposeCode"),
            "endToEndId": obj.get("endToEndId")
        })
        return _obj


