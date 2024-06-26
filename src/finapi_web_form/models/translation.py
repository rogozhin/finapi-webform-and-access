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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from finapi_web_form.models.short_translation_block import ShortTranslationBlock
from finapi_web_form.models.translation_block import TranslationBlock
from typing import Optional, Set
from typing_extensions import Self

class Translation(BaseModel):
    """
    Set of titles and subtitles for a particular language, given in the <a target='_blank' href='https://www.iso.org/iso-639-language-codes.html'>ISO-639</a> 2 letter format code, grouped by view
    """ # noqa: E501
    bank_search_view: Optional[ShortTranslationBlock] = Field(default=None, alias="bankSearchView")
    bank_selection_view: Optional[ShortTranslationBlock] = Field(default=None, alias="bankSelectionView")
    bank_login_view: Optional[TranslationBlock] = Field(default=None, alias="bankLoginView")
    redirect_bank_login_view: Optional[TranslationBlock] = Field(default=None, alias="redirectBankLoginView")
    sca_method_selection_view: Optional[ShortTranslationBlock] = Field(default=None, alias="scaMethodSelectionView")
    sca_challenge_view: Optional[ShortTranslationBlock] = Field(default=None, alias="scaChallengeView")
    account_selection_view_ais: Optional[TranslationBlock] = Field(default=None, alias="accountSelectionViewAis")
    account_selection_view_pis: Optional[TranslationBlock] = Field(default=None, alias="accountSelectionViewPis")
    data_download_view_ais: Optional[ShortTranslationBlock] = Field(default=None, alias="dataDownloadViewAis")
    partial_confirmation_view: Optional[ShortTranslationBlock] = Field(default=None, alias="partialConfirmationView")
    partial_confirmation_with_error_view: Optional[ShortTranslationBlock] = Field(default=None, alias="partialConfirmationWithErrorView")
    update_summary_view: Optional[ShortTranslationBlock] = Field(default=None, alias="updateSummaryView")
    confirmation_view: Optional[ShortTranslationBlock] = Field(default=None, alias="confirmationView")
    error_view: Optional[ShortTranslationBlock] = Field(default=None, alias="errorView")
    __properties: ClassVar[List[str]] = ["bankSearchView", "bankSelectionView", "bankLoginView", "redirectBankLoginView", "scaMethodSelectionView", "scaChallengeView", "accountSelectionViewAis", "accountSelectionViewPis", "dataDownloadViewAis", "partialConfirmationView", "partialConfirmationWithErrorView", "updateSummaryView", "confirmationView", "errorView"]

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
        """Create an instance of Translation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bank_search_view
        if self.bank_search_view:
            _dict['bankSearchView'] = self.bank_search_view.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bank_selection_view
        if self.bank_selection_view:
            _dict['bankSelectionView'] = self.bank_selection_view.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bank_login_view
        if self.bank_login_view:
            _dict['bankLoginView'] = self.bank_login_view.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redirect_bank_login_view
        if self.redirect_bank_login_view:
            _dict['redirectBankLoginView'] = self.redirect_bank_login_view.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sca_method_selection_view
        if self.sca_method_selection_view:
            _dict['scaMethodSelectionView'] = self.sca_method_selection_view.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sca_challenge_view
        if self.sca_challenge_view:
            _dict['scaChallengeView'] = self.sca_challenge_view.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account_selection_view_ais
        if self.account_selection_view_ais:
            _dict['accountSelectionViewAis'] = self.account_selection_view_ais.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account_selection_view_pis
        if self.account_selection_view_pis:
            _dict['accountSelectionViewPis'] = self.account_selection_view_pis.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_download_view_ais
        if self.data_download_view_ais:
            _dict['dataDownloadViewAis'] = self.data_download_view_ais.to_dict()
        # override the default output from pydantic by calling `to_dict()` of partial_confirmation_view
        if self.partial_confirmation_view:
            _dict['partialConfirmationView'] = self.partial_confirmation_view.to_dict()
        # override the default output from pydantic by calling `to_dict()` of partial_confirmation_with_error_view
        if self.partial_confirmation_with_error_view:
            _dict['partialConfirmationWithErrorView'] = self.partial_confirmation_with_error_view.to_dict()
        # override the default output from pydantic by calling `to_dict()` of update_summary_view
        if self.update_summary_view:
            _dict['updateSummaryView'] = self.update_summary_view.to_dict()
        # override the default output from pydantic by calling `to_dict()` of confirmation_view
        if self.confirmation_view:
            _dict['confirmationView'] = self.confirmation_view.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error_view
        if self.error_view:
            _dict['errorView'] = self.error_view.to_dict()
        # set to None if bank_search_view (nullable) is None
        # and model_fields_set contains the field
        if self.bank_search_view is None and "bank_search_view" in self.model_fields_set:
            _dict['bankSearchView'] = None

        # set to None if bank_selection_view (nullable) is None
        # and model_fields_set contains the field
        if self.bank_selection_view is None and "bank_selection_view" in self.model_fields_set:
            _dict['bankSelectionView'] = None

        # set to None if bank_login_view (nullable) is None
        # and model_fields_set contains the field
        if self.bank_login_view is None and "bank_login_view" in self.model_fields_set:
            _dict['bankLoginView'] = None

        # set to None if redirect_bank_login_view (nullable) is None
        # and model_fields_set contains the field
        if self.redirect_bank_login_view is None and "redirect_bank_login_view" in self.model_fields_set:
            _dict['redirectBankLoginView'] = None

        # set to None if sca_method_selection_view (nullable) is None
        # and model_fields_set contains the field
        if self.sca_method_selection_view is None and "sca_method_selection_view" in self.model_fields_set:
            _dict['scaMethodSelectionView'] = None

        # set to None if sca_challenge_view (nullable) is None
        # and model_fields_set contains the field
        if self.sca_challenge_view is None and "sca_challenge_view" in self.model_fields_set:
            _dict['scaChallengeView'] = None

        # set to None if account_selection_view_ais (nullable) is None
        # and model_fields_set contains the field
        if self.account_selection_view_ais is None and "account_selection_view_ais" in self.model_fields_set:
            _dict['accountSelectionViewAis'] = None

        # set to None if account_selection_view_pis (nullable) is None
        # and model_fields_set contains the field
        if self.account_selection_view_pis is None and "account_selection_view_pis" in self.model_fields_set:
            _dict['accountSelectionViewPis'] = None

        # set to None if data_download_view_ais (nullable) is None
        # and model_fields_set contains the field
        if self.data_download_view_ais is None and "data_download_view_ais" in self.model_fields_set:
            _dict['dataDownloadViewAis'] = None

        # set to None if partial_confirmation_view (nullable) is None
        # and model_fields_set contains the field
        if self.partial_confirmation_view is None and "partial_confirmation_view" in self.model_fields_set:
            _dict['partialConfirmationView'] = None

        # set to None if partial_confirmation_with_error_view (nullable) is None
        # and model_fields_set contains the field
        if self.partial_confirmation_with_error_view is None and "partial_confirmation_with_error_view" in self.model_fields_set:
            _dict['partialConfirmationWithErrorView'] = None

        # set to None if update_summary_view (nullable) is None
        # and model_fields_set contains the field
        if self.update_summary_view is None and "update_summary_view" in self.model_fields_set:
            _dict['updateSummaryView'] = None

        # set to None if confirmation_view (nullable) is None
        # and model_fields_set contains the field
        if self.confirmation_view is None and "confirmation_view" in self.model_fields_set:
            _dict['confirmationView'] = None

        # set to None if error_view (nullable) is None
        # and model_fields_set contains the field
        if self.error_view is None and "error_view" in self.model_fields_set:
            _dict['errorView'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Translation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bankSearchView": ShortTranslationBlock.from_dict(obj["bankSearchView"]) if obj.get("bankSearchView") is not None else None,
            "bankSelectionView": ShortTranslationBlock.from_dict(obj["bankSelectionView"]) if obj.get("bankSelectionView") is not None else None,
            "bankLoginView": TranslationBlock.from_dict(obj["bankLoginView"]) if obj.get("bankLoginView") is not None else None,
            "redirectBankLoginView": TranslationBlock.from_dict(obj["redirectBankLoginView"]) if obj.get("redirectBankLoginView") is not None else None,
            "scaMethodSelectionView": ShortTranslationBlock.from_dict(obj["scaMethodSelectionView"]) if obj.get("scaMethodSelectionView") is not None else None,
            "scaChallengeView": ShortTranslationBlock.from_dict(obj["scaChallengeView"]) if obj.get("scaChallengeView") is not None else None,
            "accountSelectionViewAis": TranslationBlock.from_dict(obj["accountSelectionViewAis"]) if obj.get("accountSelectionViewAis") is not None else None,
            "accountSelectionViewPis": TranslationBlock.from_dict(obj["accountSelectionViewPis"]) if obj.get("accountSelectionViewPis") is not None else None,
            "dataDownloadViewAis": ShortTranslationBlock.from_dict(obj["dataDownloadViewAis"]) if obj.get("dataDownloadViewAis") is not None else None,
            "partialConfirmationView": ShortTranslationBlock.from_dict(obj["partialConfirmationView"]) if obj.get("partialConfirmationView") is not None else None,
            "partialConfirmationWithErrorView": ShortTranslationBlock.from_dict(obj["partialConfirmationWithErrorView"]) if obj.get("partialConfirmationWithErrorView") is not None else None,
            "updateSummaryView": ShortTranslationBlock.from_dict(obj["updateSummaryView"]) if obj.get("updateSummaryView") is not None else None,
            "confirmationView": ShortTranslationBlock.from_dict(obj["confirmationView"]) if obj.get("confirmationView") is not None else None,
            "errorView": ShortTranslationBlock.from_dict(obj["errorView"]) if obj.get("errorView") is not None else None
        })
        return _obj


