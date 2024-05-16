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


class CountryCode(str, Enum):
    """
    <strong>Country code:</strong> The ISO 3166 ALPHA-2 country code of the counterparty's address.
    """

    """
    allowed enum values
    """
    AD = 'AD'
    AE = 'AE'
    AF = 'AF'
    AG = 'AG'
    AI = 'AI'
    AL = 'AL'
    AM = 'AM'
    AO = 'AO'
    AQ = 'AQ'
    AR = 'AR'
    AS = 'AS'
    AT = 'AT'
    AU = 'AU'
    AW = 'AW'
    AX = 'AX'
    AZ = 'AZ'
    BA = 'BA'
    BB = 'BB'
    BD = 'BD'
    BE = 'BE'
    BF = 'BF'
    BG = 'BG'
    BH = 'BH'
    BI = 'BI'
    BJ = 'BJ'
    BL = 'BL'
    BM = 'BM'
    BN = 'BN'
    BO = 'BO'
    BQ = 'BQ'
    BR = 'BR'
    BS = 'BS'
    BT = 'BT'
    BV = 'BV'
    BW = 'BW'
    BY = 'BY'
    BZ = 'BZ'
    CA = 'CA'
    CC = 'CC'
    CD = 'CD'
    CF = 'CF'
    CG = 'CG'
    CH = 'CH'
    CI = 'CI'
    CK = 'CK'
    CL = 'CL'
    CM = 'CM'
    CN = 'CN'
    CO = 'CO'
    CR = 'CR'
    CU = 'CU'
    CV = 'CV'
    CW = 'CW'
    CX = 'CX'
    CY = 'CY'
    CZ = 'CZ'
    DE = 'DE'
    DJ = 'DJ'
    DK = 'DK'
    DM = 'DM'
    DO = 'DO'
    DZ = 'DZ'
    EC = 'EC'
    EE = 'EE'
    EG = 'EG'
    EH = 'EH'
    ER = 'ER'
    ES = 'ES'
    ET = 'ET'
    FI = 'FI'
    FJ = 'FJ'
    FK = 'FK'
    FM = 'FM'
    FO = 'FO'
    FR = 'FR'
    GA = 'GA'
    GB = 'GB'
    GD = 'GD'
    GE = 'GE'
    GF = 'GF'
    GG = 'GG'
    GH = 'GH'
    GI = 'GI'
    GL = 'GL'
    GM = 'GM'
    GN = 'GN'
    GP = 'GP'
    GQ = 'GQ'
    GR = 'GR'
    GS = 'GS'
    GT = 'GT'
    GU = 'GU'
    GW = 'GW'
    GY = 'GY'
    HK = 'HK'
    HM = 'HM'
    HN = 'HN'
    HR = 'HR'
    HT = 'HT'
    HU = 'HU'
    ID = 'ID'
    IE = 'IE'
    IL = 'IL'
    IM = 'IM'
    IN = 'IN'
    IO = 'IO'
    IQ = 'IQ'
    IR = 'IR'
    IS = 'IS'
    IT = 'IT'
    JE = 'JE'
    JM = 'JM'
    JO = 'JO'
    JP = 'JP'
    KE = 'KE'
    KG = 'KG'
    KH = 'KH'
    KI = 'KI'
    KM = 'KM'
    KN = 'KN'
    KP = 'KP'
    KR = 'KR'
    KW = 'KW'
    KY = 'KY'
    KZ = 'KZ'
    LA = 'LA'
    LB = 'LB'
    LC = 'LC'
    LI = 'LI'
    LK = 'LK'
    LR = 'LR'
    LS = 'LS'
    LT = 'LT'
    LU = 'LU'
    LV = 'LV'
    LY = 'LY'
    MA = 'MA'
    MC = 'MC'
    MD = 'MD'
    ME = 'ME'
    MF = 'MF'
    MG = 'MG'
    MH = 'MH'
    MK = 'MK'
    ML = 'ML'
    MM = 'MM'
    MN = 'MN'
    MO = 'MO'
    MP = 'MP'
    MQ = 'MQ'
    MR = 'MR'
    MS = 'MS'
    MT = 'MT'
    MU = 'MU'
    MV = 'MV'
    MW = 'MW'
    MX = 'MX'
    MY = 'MY'
    MZ = 'MZ'
    NA = 'NA'
    NC = 'NC'
    NE = 'NE'
    NF = 'NF'
    NG = 'NG'
    NI = 'NI'
    NL = 'NL'
    NO = 'NO'
    NP = 'NP'
    NR = 'NR'
    NU = 'NU'
    NZ = 'NZ'
    OM = 'OM'
    PA = 'PA'
    PE = 'PE'
    PF = 'PF'
    PG = 'PG'
    PH = 'PH'
    PK = 'PK'
    PL = 'PL'
    PM = 'PM'
    PN = 'PN'
    PR = 'PR'
    PS = 'PS'
    PT = 'PT'
    PW = 'PW'
    PY = 'PY'
    QA = 'QA'
    RE = 'RE'
    RO = 'RO'
    RS = 'RS'
    RU = 'RU'
    RW = 'RW'
    SA = 'SA'
    SB = 'SB'
    SC = 'SC'
    SD = 'SD'
    SE = 'SE'
    SG = 'SG'
    SH = 'SH'
    SI = 'SI'
    SJ = 'SJ'
    SK = 'SK'
    SL = 'SL'
    SM = 'SM'
    SN = 'SN'
    SO = 'SO'
    SR = 'SR'
    SS = 'SS'
    ST = 'ST'
    SV = 'SV'
    SX = 'SX'
    SY = 'SY'
    SZ = 'SZ'
    TC = 'TC'
    TD = 'TD'
    TF = 'TF'
    TG = 'TG'
    TH = 'TH'
    TJ = 'TJ'
    TK = 'TK'
    TL = 'TL'
    TM = 'TM'
    TN = 'TN'
    TO = 'TO'
    TR = 'TR'
    TT = 'TT'
    TV = 'TV'
    TW = 'TW'
    TZ = 'TZ'
    UA = 'UA'
    UG = 'UG'
    UM = 'UM'
    US = 'US'
    UY = 'UY'
    UZ = 'UZ'
    VA = 'VA'
    VC = 'VC'
    VE = 'VE'
    VG = 'VG'
    VI = 'VI'
    VN = 'VN'
    VU = 'VU'
    WF = 'WF'
    WS = 'WS'
    XK = 'XK'
    YE = 'YE'
    YT = 'YT'
    ZA = 'ZA'
    ZM = 'ZM'
    ZW = 'ZW'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CountryCode from a JSON string"""
        return cls(json.loads(json_str))


