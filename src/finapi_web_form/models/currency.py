# coding: utf-8

"""
    finAPI Web Form 2.0

    The following pages give you some general information on how to use our APIs.<br/>The actual API services documentation then follows further below. You can use the menu to jump between API sections.<br/><br/>This page has a built-in HTTP(S) client, so you can test the services directly from within this page, by filling in the request parameters and/or body in the respective services, and then hitting the TRY button. Note that you need to be authorized to make a successful API call. To authorize, refer to the '<a target='_blank' href='https://docs.finapi.io/?product=access#tag--Authorization'>Authorization</a>' section of Access, or in case you already have a valid user token, just use the QUICK AUTH on the left.<br/>Please also remember that all user management functions should be looked up in <a target='_blank' href='https://docs.finapi.io/?product=access'>Access</a>.<br/><br/>You should also check out the <a target='_blank' href='https://documentation.finapi.io/webform/'>Web Form 2.0 Public Documentation</a> as well as <a target='_blank' href='https://documentation.finapi.io/access/'>Access Public Documentation</a> for more information. If you need any help with the API, contact <a href='mailto:support@finapi.io'>support@finapi.io</a>.<br/><h2 id=\"general-information\">General information</h2><h3 id=\"general-request-ids\"><strong>Request IDs</strong></h3>With any API call, you can pass a request ID via a header with name \"X-Request-Id\". The request ID can be an arbitrary string with up to 255 characters. Passing a longer string will result in an error.<br/><br/>If you don't pass a request ID for a call, finAPI will generate a random ID internally.<br/><br/>The request ID is always returned back in the response of a service, as a header with name \"X-Request-Id\".<br/><br/>We highly recommend to always pass a (preferably unique) request ID, and include it into your client application logs whenever you make a request or receive a response(especially in the case of an error response). finAPI is also logging request IDs on its end. Having a request ID can help the finAPI support team to work more efficiently and solve tickets faster.<h3 id=\"type-coercion\"><strong>Type Coercion</strong></h3>In order to ease the integration for some languages, which do not natively support high precision number representations, Web Form 2.0 API supports relax type binding for the openAPI type <code>number</code>, which is used for money amount fields. If you use one of those languages, to avoid precision errors that can appear from <code>float</code> values, you can pass the amount as a <code>string</code>.<h3 id=\"general-faq\"><strong>FAQ</strong></h3><strong>Is there a finAPI SDK?</strong><br/>Currently we do not offer a native SDK, but there is the option to generate an SDKfor almost any target language via OpenAPI. Use the 'Download SDK' button on this page for SDK generation.<br/><br/><strong>Why do I need to keep authorizing when calling services on this page?</strong><br/>This page is a \"one-page-app\". Reloading the page resets the OAuth authorization context. There is generally no need to reload the page, so just don't do it and your authorization will persist.

    The version of the OpenAPI document: 2.709.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class Currency(str, Enum):
    """
    <strong>Currency:</strong> The <a target='_blank' href='https://www.iso.org/iso-4217-currency-codes.html'>ISO-4217</a> currency code of the amount.<br/>At the moment, the only possible currency we accept here is:<br/>&bull; for direct debits and standing orders - <code>EUR</code> only;<br/>&bull; for payments with an account - the currency associated with the account. (Currently we support SEPA (EUR) and CZ domestic payments (CZK). For the rest, it will work on a best-effort basis.)
    """

    """
    allowed enum values
    """
    AED = 'AED'
    AFN = 'AFN'
    ALL = 'ALL'
    AMD = 'AMD'
    ANG = 'ANG'
    AOA = 'AOA'
    ARS = 'ARS'
    AUD = 'AUD'
    AWG = 'AWG'
    AZN = 'AZN'
    BAM = 'BAM'
    BBD = 'BBD'
    BDT = 'BDT'
    BGN = 'BGN'
    BHD = 'BHD'
    BIF = 'BIF'
    BMD = 'BMD'
    BND = 'BND'
    BOB = 'BOB'
    BOV = 'BOV'
    BRL = 'BRL'
    BSD = 'BSD'
    BTN = 'BTN'
    BWP = 'BWP'
    BYN = 'BYN'
    BZD = 'BZD'
    CAD = 'CAD'
    CDF = 'CDF'
    CHE = 'CHE'
    CHF = 'CHF'
    CHN = 'CHN'
    CHW = 'CHW'
    CLF = 'CLF'
    CLP = 'CLP'
    CNY = 'CNY'
    COP = 'COP'
    COU = 'COU'
    CRC = 'CRC'
    CUC = 'CUC'
    CUP = 'CUP'
    CVE = 'CVE'
    CZK = 'CZK'
    DJF = 'DJF'
    DKK = 'DKK'
    DOP = 'DOP'
    DZD = 'DZD'
    EGP = 'EGP'
    ERN = 'ERN'
    ETB = 'ETB'
    EUR = 'EUR'
    FJD = 'FJD'
    FKP = 'FKP'
    GBP = 'GBP'
    GEL = 'GEL'
    GGP = 'GGP'
    GHS = 'GHS'
    GIP = 'GIP'
    GMD = 'GMD'
    GNF = 'GNF'
    GTQ = 'GTQ'
    GYD = 'GYD'
    HKD = 'HKD'
    HNL = 'HNL'
    HRK = 'HRK'
    HTG = 'HTG'
    HUF = 'HUF'
    IDR = 'IDR'
    ILS = 'ILS'
    IMP = 'IMP'
    INR = 'INR'
    IQD = 'IQD'
    IRR = 'IRR'
    ISK = 'ISK'
    JEP = 'JEP'
    JMD = 'JMD'
    JOD = 'JOD'
    JPY = 'JPY'
    KES = 'KES'
    KGS = 'KGS'
    KHR = 'KHR'
    KID = 'KID'
    KMF = 'KMF'
    KPW = 'KPW'
    KRW = 'KRW'
    KWD = 'KWD'
    KYD = 'KYD'
    KZT = 'KZT'
    LAK = 'LAK'
    LBP = 'LBP'
    LKR = 'LKR'
    LRD = 'LRD'
    LSL = 'LSL'
    LYD = 'LYD'
    MAD = 'MAD'
    MDL = 'MDL'
    MGA = 'MGA'
    MKD = 'MKD'
    MMK = 'MMK'
    MNT = 'MNT'
    MOP = 'MOP'
    MRU = 'MRU'
    MUR = 'MUR'
    MVR = 'MVR'
    MWK = 'MWK'
    MXN = 'MXN'
    MXV = 'MXV'
    MYR = 'MYR'
    MZN = 'MZN'
    NAD = 'NAD'
    NGN = 'NGN'
    NIO = 'NIO'
    NIS = 'NIS'
    NOK = 'NOK'
    NPR = 'NPR'
    NTD = 'NTD'
    NZD = 'NZD'
    OMR = 'OMR'
    PAB = 'PAB'
    PEN = 'PEN'
    PGK = 'PGK'
    PHP = 'PHP'
    PKR = 'PKR'
    PLN = 'PLN'
    PRB = 'PRB'
    PYG = 'PYG'
    QAR = 'QAR'
    RMB = 'RMB'
    RON = 'RON'
    RSD = 'RSD'
    RUB = 'RUB'
    RWF = 'RWF'
    SAR = 'SAR'
    SBD = 'SBD'
    SCR = 'SCR'
    SDG = 'SDG'
    SEK = 'SEK'
    SGD = 'SGD'
    SHP = 'SHP'
    SLL = 'SLL'
    SLS = 'SLS'
    SOS = 'SOS'
    SRD = 'SRD'
    SSP = 'SSP'
    STN = 'STN'
    SVC = 'SVC'
    SYP = 'SYP'
    SZL = 'SZL'
    THB = 'THB'
    TJS = 'TJS'
    TMT = 'TMT'
    TND = 'TND'
    TOP = 'TOP'
    TRY = 'TRY'
    TTD = 'TTD'
    TVD = 'TVD'
    TWD = 'TWD'
    TZS = 'TZS'
    UAH = 'UAH'
    UGX = 'UGX'
    USD = 'USD'
    USN = 'USN'
    UYI = 'UYI'
    UYU = 'UYU'
    UYW = 'UYW'
    UZS = 'UZS'
    VEF = 'VEF'
    VES = 'VES'
    VND = 'VND'
    VUV = 'VUV'
    WST = 'WST'
    XAF = 'XAF'
    XAG = 'XAG'
    XAU = 'XAU'
    XBA = 'XBA'
    XBB = 'XBB'
    XBC = 'XBC'
    XBD = 'XBD'
    XCD = 'XCD'
    XDR = 'XDR'
    XOF = 'XOF'
    XPD = 'XPD'
    XPF = 'XPF'
    XPT = 'XPT'
    XSU = 'XSU'
    XTS = 'XTS'
    XUA = 'XUA'
    XXX = 'XXX'
    YER = 'YER'
    ZAR = 'ZAR'
    ZMW = 'ZMW'
    ZWB = 'ZWB'
    ZWL = 'ZWL'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Currency from a JSON string"""
        return cls(json.loads(json_str))


