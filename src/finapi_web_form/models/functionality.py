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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from finapi_web_form.models.language import Language
from typing import Optional, Set
from typing_extensions import Self

class Functionality(BaseModel):
    """
    Customization of web form functionality
    """ # noqa: E501
    progress_bar: Optional[StrictStr] = Field(default=None, description="Whether a progress bar is shown on the web form, letting the user know on which step he is.<br/>&bull; <code>RENDER</code> - the progress bar will be shown;<br/>&bull; <code>HIDDEN</code> - the progress bar will NOT be shown.<br/><strong>NOTE:</strong> If no value is provided, then the following value will be applied by default when web form is opened: <code>RENDER</code>.", alias="progressBar")
    bank_login_hint: Optional[StrictStr] = Field(default=None, description="How the bank login hint will be shown to the end user<br/>&bull; <code>EXPANDED</code> - the user will see the login hint and will have the option to collapse it;<br/>&bull; <code>COLLAPSED</code> - the login hint will be collapsed and the user can see it if he expands the field;<br/>&bull; <code>HIDDEN</code> - the login hint is hidden and the user cannot see it.<br/><strong>NOTE:</strong> If no value is provided, then the following value will be applied by default when web form is opened: <code>EXPANDED</code>.", alias="bankLoginHint")
    store_secrets: Optional[StrictStr] = Field(default=None, description="Whether the user will have a checkbox to ask for storing login secrets (like a PIN) in finAPI or not.<br/>&bull; <code>RENDER</code> - the checkbox will be shown;<br/>&bull; <code>HIDDEN</code> - the checkbox will NOT be shown;<br/>&bull; <code>MANDATORY</code> - the checkbox will be shown and it will be mandatory for the end user to check it in order to continue.<br/>&bull; <code>IMPLICIT_APPROVAL</code> - the checkbox will NOT be shown but login secrets will nevertheless be stored;<br/>&nbsp;&nbsp;&nbsp;&nbsp;<strong>NOTE:</strong> This value will also automatically store the TAN method. This value can be applied ONLY by our support team. Please contact <a href='mailto:support@finapi.io'>support@finapi.io</a> with the <code>profile.id</code> as soon as you have finalized the customization for other parameters.<br/><strong>NOTE:</strong> If no value is provided, then the following value will be applied by default when web form is opened: <code>RENDER</code>.", alias="storeSecrets")
    bank_details: Optional[StrictStr] = Field(default=None, description="Whether the user will be allowed to change the selected bank, in case a BLZ/BIC/IBAN was sent in the API request by the client.<br/>&bull; <code>LOCKED</code> - the user will be directly routed to login to the pre-selected bank;<br/>&bull; <code>EDITABLE</code> - the user will see the pre-selected bank and have the option to change it.<br/><strong>NOTE:</strong> If no value is provided, then the following value will be applied by default when web form is opened: <code>LOCKED</code>.", alias="bankDetails")
    header: Optional[StrictStr] = Field(default=None, description="Whether the header will be displayed on the web form.<br/>&bull; <code>RENDER</code> - the header will be shown;<br/>&bull; <code>HIDDEN</code> - the header will NOT be shown.<br/><strong>NOTE:</strong> If no value is provided, then the following value will be applied by default when web form is opened: <code>RENDER</code>.")
    language: Optional[Language] = None
    skip_confirmation_view: Optional[StrictBool] = Field(default=None, description="When the web form is completed successfully, it determines whether the last view will be rendered. It applies to embedded and standalone web forms. It also applies to all endpoints in the \"Account Information Services\" and \"Payment Initiation Services\".<br/>If you are embedding the web form in your application, please set up appropriate handling for the 'onComplete' method to take advantage of the feature.<br/><strong>NOTE:</strong> If no value is provided, then the following value will be applied by default when web form is opened: <code>false</code>", alias="skipConfirmationView")
    render_account_selection_view: Optional[StrictBool] = Field(default=None, description="Whether the Web Form will render the \"Account Selection View\" for the end-user to choose which of the imported accounts should be saved to the database and available on the customer application.<br/><strong>NOTE:</strong> If no value is provided, then the following value will be applied by default when web form is opened: <code>false</code>", alias="renderAccountSelectionView")
    hide_payment_summary: Optional[StrictBool] = Field(default=None, description="Whether the entire payment summary is rendered on the Web Form. When set to TRUE, the counterpart data is not rendered on the Payment Summary of the Web Form.<br/><strong>NOTE:</strong> This value can be applied ONLY by our support team. Please contact <a href='mailto:support@finapi.io'>support@finapi.io</a> with the <code>profile.id</code> as soon as you have finalized the customization for other parameters.<br/><strong>NOTE:</strong> If no value is provided, then the following value will be applied by default when web form is opened: <code>false</code>", alias="hidePaymentSummary")
    __properties: ClassVar[List[str]] = ["progressBar", "bankLoginHint", "storeSecrets", "bankDetails", "header", "language", "skipConfirmationView", "renderAccountSelectionView", "hidePaymentSummary"]

    @field_validator('progress_bar')
    def progress_bar_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['RENDER', 'HIDDEN']):
            raise ValueError("must be one of enum values ('RENDER', 'HIDDEN')")
        return value

    @field_validator('bank_login_hint')
    def bank_login_hint_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['EXPANDED', 'COLLAPSED', 'HIDDEN']):
            raise ValueError("must be one of enum values ('EXPANDED', 'COLLAPSED', 'HIDDEN')")
        return value

    @field_validator('store_secrets')
    def store_secrets_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['RENDER', 'HIDDEN', 'MANDATORY', 'IMPLICIT_APPROVAL']):
            raise ValueError("must be one of enum values ('RENDER', 'HIDDEN', 'MANDATORY', 'IMPLICIT_APPROVAL')")
        return value

    @field_validator('bank_details')
    def bank_details_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LOCKED', 'EDITABLE']):
            raise ValueError("must be one of enum values ('LOCKED', 'EDITABLE')")
        return value

    @field_validator('header')
    def header_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['RENDER', 'HIDDEN']):
            raise ValueError("must be one of enum values ('RENDER', 'HIDDEN')")
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
        """Create an instance of Functionality from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of language
        if self.language:
            _dict['language'] = self.language.to_dict()
        # set to None if progress_bar (nullable) is None
        # and model_fields_set contains the field
        if self.progress_bar is None and "progress_bar" in self.model_fields_set:
            _dict['progressBar'] = None

        # set to None if bank_login_hint (nullable) is None
        # and model_fields_set contains the field
        if self.bank_login_hint is None and "bank_login_hint" in self.model_fields_set:
            _dict['bankLoginHint'] = None

        # set to None if store_secrets (nullable) is None
        # and model_fields_set contains the field
        if self.store_secrets is None and "store_secrets" in self.model_fields_set:
            _dict['storeSecrets'] = None

        # set to None if bank_details (nullable) is None
        # and model_fields_set contains the field
        if self.bank_details is None and "bank_details" in self.model_fields_set:
            _dict['bankDetails'] = None

        # set to None if header (nullable) is None
        # and model_fields_set contains the field
        if self.header is None and "header" in self.model_fields_set:
            _dict['header'] = None

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict['language'] = None

        # set to None if skip_confirmation_view (nullable) is None
        # and model_fields_set contains the field
        if self.skip_confirmation_view is None and "skip_confirmation_view" in self.model_fields_set:
            _dict['skipConfirmationView'] = None

        # set to None if render_account_selection_view (nullable) is None
        # and model_fields_set contains the field
        if self.render_account_selection_view is None and "render_account_selection_view" in self.model_fields_set:
            _dict['renderAccountSelectionView'] = None

        # set to None if hide_payment_summary (nullable) is None
        # and model_fields_set contains the field
        if self.hide_payment_summary is None and "hide_payment_summary" in self.model_fields_set:
            _dict['hidePaymentSummary'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Functionality from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "progressBar": obj.get("progressBar"),
            "bankLoginHint": obj.get("bankLoginHint"),
            "storeSecrets": obj.get("storeSecrets"),
            "bankDetails": obj.get("bankDetails"),
            "header": obj.get("header"),
            "language": Language.from_dict(obj["language"]) if obj.get("language") is not None else None,
            "skipConfirmationView": obj.get("skipConfirmationView"),
            "renderAccountSelectionView": obj.get("renderAccountSelectionView"),
            "hidePaymentSummary": obj.get("hidePaymentSummary")
        })
        return _obj


