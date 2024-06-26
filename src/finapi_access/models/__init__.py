# coding: utf-8

# flake8: noqa
"""
    finAPI Access V2

    <strong>RESTful API for Account Information Services (AIS) and Payment Initiation Services (PIS)</strong> <br/> <strong>Application Version:</strong> 2.38.0 <br/>  The following pages give you some general information on how to use our APIs.<br/> The actual API services documentation then follows further below. You can use the menu to jump between API sections. <br/> <br/> This page has a built-in HTTP(S) client, so you can test the services directly from within this page, by filling in the request parameters and/or body in the respective services, and then hitting the TRY button. Note that you need to be authorized to make a successful API call. To authorize, refer to the 'Authorization' section of the API, or just use the OAUTH button that can be found near the TRY button. <br/>  <h2 id=\"general-information\">General information</h2>  <h3 id=\"general-error-responses\"><strong>Error Responses</strong></h3> When an API call returns with an error, then in general it has the structure shown in the following example:  <pre> {   \"errors\": [     {       \"message\": \"Interface 'FINTS_SERVER' is not supported for this operation.\",       \"code\": \"BAD_REQUEST\",       \"type\": \"TECHNICAL\"     }   ],   \"date\": \"2020-11-19T16:54:06.854+01:00\",   \"requestId\": \"selfgen-312042e7-df55-47e4-bffd-956a68ef37b5\",   \"endpoint\": \"POST /api/v2/bankConnections/import\",   \"authContext\": \"1/21\",   \"bank\": \"DEMO0002 - finAPI Test Redirect Bank (id: 280002, location: none)\" } </pre>  If an API call requires an additional authentication by the user, HTTP code 510 is returned and the error response contains the additional \"multiStepAuthentication\" object, see the following example:  <pre> {   \"errors\": [     {       \"message\": \"Es ist eine zusätzliche Authentifizierung erforderlich. Bitte geben Sie folgenden Code an: 123456\",       \"code\": \"ADDITIONAL_AUTHENTICATION_REQUIRED\",       \"type\": \"BUSINESS\",       \"multiStepAuthentication\": {         \"hash\": \"678b13f4be9ed7d981a840af8131223a\",         \"status\": \"CHALLENGE_RESPONSE_REQUIRED\",         \"challengeMessage\": \"Es ist eine zusätzliche Authentifizierung erforderlich. Bitte geben Sie folgenden Code an: 123456\",         \"answerFieldLabel\": \"TAN\",         \"redirectUrl\": null,         \"redirectContext\": null,         \"redirectContextField\": null,         \"twoStepProcedures\": null,         \"photoTanMimeType\": null,         \"photoTanData\": null,         \"opticalData\": null,         \"opticalDataAsReinerSct\": false       }     }   ],   \"date\": \"2019-11-29T09:51:55.931+01:00\",   \"requestId\": \"selfgen-45059c99-1b14-4df7-9bd3-9d5f126df294\",   \"endpoint\": \"POST /api/v2/bankConnections/import\",   \"authContext\": \"1/18\",   \"bank\": \"DEMO0001 - finAPI Test Bank\" } </pre>  An exception to this error format are API authentication errors, where the following structure is returned:  <pre> {   \"error\": \"invalid_token\",   \"error_description\": \"Invalid access token: cccbce46-xxxx-xxxx-xxxx-xxxxxxxxxx\" } </pre>  <h3 id=\"general-paging\"><strong>Paging</strong></h3> API services that may potentially return a lot of data implement paging. They return a limited number of entries within a \"page\". Further entries must be fetched with subsequent calls. <br/><br/> Any API service that implements paging provides the following input parameters:<br/> &bull; \"page\": the number of the page to be retrieved (starting with 1).<br/> &bull; \"perPage\": the number of entries within a page. The default and maximum value is stated in the documentation of the respective services.  A paged response contains an additional \"paging\" object with the following structure:  <pre> {   ...   ,   \"paging\": {     \"page\": 1,     \"perPage\": 20,     \"pageCount\": 234,     \"totalCount\": 4662   } } </pre>  <h3 id=\"general-internationalization\"><strong>Internationalization</strong></h3> The finAPI services support internationalization which means you can define the language you prefer for API service responses. <br/><br/> The following languages are available: German, English, Czech, Slovak. <br/><br/> The preferred language can be defined by providing the official HTTP <strong>Accept-Language</strong> header. <br/><br/> finAPI reacts on the official iso language codes &quot;de&quot;, &quot;en&quot;, &quot;cs&quot; and &quot;sk&quot; for the named languages. Additional subtags supported by the Accept-Language header may be provided, e.g. &quot;en-US&quot;, but are ignored. <br/> If no Accept-Language header is given, German is used as the default language. <br/><br/> Exceptions:<br/> &bull; Bank login hints and login fields are only available in the language of the bank and not being translated.<br/> &bull; Direct messages from the bank systems typically returned as BUSINESS errors will not be translated.<br/> &bull; BUSINESS errors created by finAPI directly are available in German and English.<br/> &bull; TECHNICAL errors messages meant for developers are mostly in English, but also may be translated.  <h3 id=\"general-request-ids\"><strong>Request IDs</strong></h3> With any API call, you can pass a request ID via a header with name \"X-Request-Id\". The request ID can be an arbitrary string with up to 255 characters. Passing a longer string will result in an error. <br/><br/> If you don't pass a request ID for a call, finAPI will generate a random ID internally. <br/><br/> The request ID is always returned back in the response of a service, as a header with name \"X-Request-Id\". <br/><br/> We highly recommend to always pass a (preferably unique) request ID, and include it into your client application logs whenever you make a request or receive a response (especially in the case of an error response). finAPI is also logging request IDs on its end. Having a request ID can help the finAPI support team to work more efficiently and solve tickets faster.  <h3 id=\"general-overriding-http-methods\"><strong>Overriding HTTP methods</strong></h3> Some HTTP clients do not support the HTTP methods PATCH or DELETE. If you are using such a client in your application, you can use a POST request instead with a special HTTP header indicating the originally intended HTTP method. <br/><br/> The header's name is <strong>X-HTTP-Method-Override</strong>. Set its value to either <strong>PATCH</strong> or <strong>DELETE</strong>. POST Requests having this header set will be treated either as PATCH or DELETE by the finAPI servers. <br/><br/> Example: <br/><br/> <strong>X-HTTP-Method-Override: PATCH</strong><br/> POST /api/v2/label/51<br/> {\"name\": \"changed label\"}<br/><br/> will be interpreted by finAPI as:<br/><br/> PATCH /api/v2/label/51<br/> {\"name\": \"changed label\"}<br/>  <h3 id=\"general-user-metadata\"><strong>User metadata</strong></h3> With the migration to PSD2 APIs, a new term called \"User metadata\" (also known as \"PSU metadata\") has been introduced to the API. This user metadata aims to inform the banking API if there was a real end-user behind an HTTP request or if the request was triggered by a system (e.g. by an automatic batch update). In the latter case, the bank may apply some restrictions such as limiting the number of HTTP requests for a single consent. Also, some operations may be forbidden entirely by the banking API. For example, some banks do not allow issuing a new consent without the end-user being involved. Therefore, it is certainly necessary and obligatory for the customer to provide the PSU metadata for such operations. <br/><br/> As finAPI does not have direct interaction with the end-user, it is the client application's responsibility to provide all the necessary information about the end-user. This must be done by sending additional headers with every request triggered on behalf of the end-user. <br/><br/> At the moment, the following headers are supported by the API:<br/> &bull; \"PSU-IP-Address\" - the IP address of the user's device. It has to be an IPv4 address, as some banks cannot work with IPv6 addresses. If a non-IPv4 address is passed, we will replace the value with our own IPv4 address as a fallback.<br/> &bull; \"PSU-Device-OS\" - the user's device and/or operating system identification.<br/> &bull; \"PSU-User-Agent\" - the user's web browser or other client device identification.  <h3 id=\"general-faq\"><strong>FAQ</strong></h3> <strong>Is there a finAPI SDK?</strong> <br/> Currently we do not offer a native SDK, but there is the option to generate an SDK for almost any target language via OpenAPI. Use the 'Download SDK' button on this page for SDK generation. <br/> <br/> <strong>How can I enable finAPI's automatic batch update?</strong> <br/> Currently there is no way to set up the batch update via the API. Please contact support@finapi.io for this. <br/> <br/> <strong>Why do I need to keep authorizing when calling services on this page?</strong> <br/> This page is a \"one-page-app\". Reloading the page resets the OAuth authorization context. There is generally no need to reload the page, so just don't do it and your authorization will persist. 

    The version of the OpenAPI document: 2024.18.1
    Contact: kontakt@finapi.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from finapi_access.models.access_token import AccessToken
from finapi_access.models.account import Account
from finapi_access.models.account_capability import AccountCapability
from finapi_access.models.account_interface import AccountInterface
from finapi_access.models.account_interface_payment_capabilities import AccountInterfacePaymentCapabilities
from finapi_access.models.account_list import AccountList
from finapi_access.models.account_params import AccountParams
from finapi_access.models.account_reference import AccountReference
from finapi_access.models.account_status import AccountStatus
from finapi_access.models.account_type import AccountType
from finapi_access.models.bad_credentials_error import BadCredentialsError
from finapi_access.models.bank import Bank
from finapi_access.models.bank_connection import BankConnection
from finapi_access.models.bank_connection_interface import BankConnectionInterface
from finapi_access.models.bank_connection_list import BankConnectionList
from finapi_access.models.bank_connection_owner import BankConnectionOwner
from finapi_access.models.bank_consent import BankConsent
from finapi_access.models.bank_consent_status import BankConsentStatus
from finapi_access.models.bank_group import BankGroup
from finapi_access.models.bank_image import BankImage
from finapi_access.models.bank_interface import BankInterface
from finapi_access.models.bank_interface_login_field import BankInterfaceLoginField
from finapi_access.models.bank_interface_payment_capabilities import BankInterfacePaymentCapabilities
from finapi_access.models.bank_interface_payment_constraints import BankInterfacePaymentConstraints
from finapi_access.models.bank_interface_property import BankInterfaceProperty
from finapi_access.models.banking_interface import BankingInterface
from finapi_access.models.cash_flow import CashFlow
from finapi_access.models.cash_flow_list import CashFlowList
from finapi_access.models.categorization_check_result import CategorizationCheckResult
from finapi_access.models.categorization_check_results import CategorizationCheckResults
from finapi_access.models.categorization_rule_direction import CategorizationRuleDirection
from finapi_access.models.categorization_status import CategorizationStatus
from finapi_access.models.category import Category
from finapi_access.models.category_params import CategoryParams
from finapi_access.models.certis_transaction_data import CertisTransactionData
from finapi_access.models.change_client_credentials_params import ChangeClientCredentialsParams
from finapi_access.models.check_categorization_data import CheckCategorizationData
from finapi_access.models.check_categorization_transaction_data import CheckCategorizationTransactionData
from finapi_access.models.client_configuration import ClientConfiguration
from finapi_access.models.client_configuration_params import ClientConfigurationParams
from finapi_access.models.connect_interface_params import ConnectInterfaceParams
from finapi_access.models.counterpart_address_data import CounterpartAddressData
from finapi_access.models.create_direct_debit_params import CreateDirectDebitParams
from finapi_access.models.create_money_transfer_params import CreateMoneyTransferParams
from finapi_access.models.create_standing_order_params import CreateStandingOrderParams
from finapi_access.models.currency import Currency
from finapi_access.models.daily_balance import DailyBalance
from finapi_access.models.daily_balance_list import DailyBalanceList
from finapi_access.models.delete_consent import DeleteConsent
from finapi_access.models.delete_consent_result import DeleteConsentResult
from finapi_access.models.direct_debit_order_params import DirectDebitOrderParams
from finapi_access.models.direct_debit_sequence_type import DirectDebitSequenceType
from finapi_access.models.direct_debit_type import DirectDebitType
from finapi_access.models.domestic_money_transfer_constraints import DomesticMoneyTransferConstraints
from finapi_access.models.domestic_money_transfer_mandatory_fields import DomesticMoneyTransferMandatoryFields
from finapi_access.models.edit_bank_connection_params import EditBankConnectionParams
from finapi_access.models.edit_category_params import EditCategoryParams
from finapi_access.models.edit_tpp_credential_params import EditTppCredentialParams
from finapi_access.models.enabled_products import EnabledProducts
from finapi_access.models.error_code import ErrorCode
from finapi_access.models.error_details import ErrorDetails
from finapi_access.models.error_message import ErrorMessage
from finapi_access.models.error_type import ErrorType
from finapi_access.models.execute_password_change_params import ExecutePasswordChangeParams
from finapi_access.models.iso3166_alpha2_codes import ISO3166Alpha2Codes
from finapi_access.models.iban_rule import IbanRule
from finapi_access.models.iban_rule_identifiers_params import IbanRuleIdentifiersParams
from finapi_access.models.iban_rule_list import IbanRuleList
from finapi_access.models.iban_rule_params import IbanRuleParams
from finapi_access.models.iban_rules_params import IbanRulesParams
from finapi_access.models.identifier_list import IdentifierList
from finapi_access.models.import_bank_connection_params import ImportBankConnectionParams
from finapi_access.models.keyword_rule import KeywordRule
from finapi_access.models.keyword_rule_identifiers_params import KeywordRuleIdentifiersParams
from finapi_access.models.keyword_rule_list import KeywordRuleList
from finapi_access.models.keyword_rule_params import KeywordRuleParams
from finapi_access.models.keyword_rules_params import KeywordRulesParams
from finapi_access.models.label import Label
from finapi_access.models.label_params import LabelParams
from finapi_access.models.language import Language
from finapi_access.models.login_credential import LoginCredential
from finapi_access.models.login_credential_resource import LoginCredentialResource
from finapi_access.models.mandator_license import MandatorLicense
from finapi_access.models.mock_account_data import MockAccountData
from finapi_access.models.mock_bank_connection_update import MockBankConnectionUpdate
from finapi_access.models.mock_batch_update_params import MockBatchUpdateParams
from finapi_access.models.money_transfer_order_params import MoneyTransferOrderParams
from finapi_access.models.monthly_user_stats import MonthlyUserStats
from finapi_access.models.msa_status import MsaStatus
from finapi_access.models.multi_step_authentication_callback import MultiStepAuthenticationCallback
from finapi_access.models.multi_step_authentication_challenge import MultiStepAuthenticationChallenge
from finapi_access.models.new_transaction import NewTransaction
from finapi_access.models.notification_rule import NotificationRule
from finapi_access.models.notification_rule_list import NotificationRuleList
from finapi_access.models.notification_rule_params import NotificationRuleParams
from finapi_access.models.order_initiation_status import OrderInitiationStatus
from finapi_access.models.pageable_bank_list import PageableBankList
from finapi_access.models.pageable_category_list import PageableCategoryList
from finapi_access.models.pageable_iban_rule_list import PageableIbanRuleList
from finapi_access.models.pageable_keyword_rule_list import PageableKeywordRuleList
from finapi_access.models.pageable_label_list import PageableLabelList
from finapi_access.models.pageable_payment_resources import PageablePaymentResources
from finapi_access.models.pageable_pending_transaction_resources import PageablePendingTransactionResources
from finapi_access.models.pageable_security_list import PageableSecurityList
from finapi_access.models.pageable_standing_order_resources import PageableStandingOrderResources
from finapi_access.models.pageable_tpp_authentication_group_resources import PageableTppAuthenticationGroupResources
from finapi_access.models.pageable_tpp_certificate_list import PageableTppCertificateList
from finapi_access.models.pageable_tpp_credential_resources import PageableTppCredentialResources
from finapi_access.models.pageable_transaction_list import PageableTransactionList
from finapi_access.models.pageable_user_info_list import PageableUserInfoList
from finapi_access.models.paging import Paging
from finapi_access.models.password_changing_resource import PasswordChangingResource
from finapi_access.models.payment import Payment
from finapi_access.models.payment_type import PaymentType
from finapi_access.models.paypal_transaction_data import PaypalTransactionData
from finapi_access.models.pending_transaction import PendingTransaction
from finapi_access.models.preferred_consent_type import PreferredConsentType
from finapi_access.models.product import Product
from finapi_access.models.remove_interface_params import RemoveInterfaceParams
from finapi_access.models.request_password_change_params import RequestPasswordChangeParams
from finapi_access.models.response_message import ResponseMessage
from finapi_access.models.security import Security
from finapi_access.models.security_position_quantity_nominal_type import SecurityPositionQuantityNominalType
from finapi_access.models.security_position_quote_type import SecurityPositionQuoteType
from finapi_access.models.sepa_money_transfer_constraints import SepaMoneyTransferConstraints
from finapi_access.models.sepa_money_transfer_counterpart_address_mandatory_fields import SepaMoneyTransferCounterpartAddressMandatoryFields
from finapi_access.models.sepa_money_transfer_mandatory_fields import SepaMoneyTransferMandatoryFields
from finapi_access.models.split_transactions_params import SplitTransactionsParams
from finapi_access.models.standing_order import StandingOrder
from finapi_access.models.standing_order_frequency import StandingOrderFrequency
from finapi_access.models.sub_transaction_params import SubTransactionParams
from finapi_access.models.submit_payment_params import SubmitPaymentParams
from finapi_access.models.submit_standing_order_params import SubmitStandingOrderParams
from finapi_access.models.switch_api_version_params import SwitchApiVersionParams
from finapi_access.models.tpp_authentication_group import TppAuthenticationGroup
from finapi_access.models.tpp_certificate import TppCertificate
from finapi_access.models.tpp_certificate_params import TppCertificateParams
from finapi_access.models.tpp_certificate_type import TppCertificateType
from finapi_access.models.tpp_credentials import TppCredentials
from finapi_access.models.tpp_credentials_params import TppCredentialsParams
from finapi_access.models.train_categorization_data import TrainCategorizationData
from finapi_access.models.train_categorization_transaction_data import TrainCategorizationTransactionData
from finapi_access.models.transaction import Transaction
from finapi_access.models.transaction_direction import TransactionDirection
from finapi_access.models.trigger_categorization_params import TriggerCategorizationParams
from finapi_access.models.two_step_procedure import TwoStepProcedure
from finapi_access.models.update_bank_connection_params import UpdateBankConnectionParams
from finapi_access.models.update_multiple_transactions_params import UpdateMultipleTransactionsParams
from finapi_access.models.update_result import UpdateResult
from finapi_access.models.update_result_status import UpdateResultStatus
from finapi_access.models.update_transactions_params import UpdateTransactionsParams
from finapi_access.models.user import User
from finapi_access.models.user_create_params import UserCreateParams
from finapi_access.models.user_identifiers_list import UserIdentifiersList
from finapi_access.models.user_identifiers_params import UserIdentifiersParams
from finapi_access.models.user_info import UserInfo
from finapi_access.models.user_update_params import UserUpdateParams
from finapi_access.models.verification_status_resource import VerificationStatusResource
