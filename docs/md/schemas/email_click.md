# EmailClick

- [1. Property `EmailClick > link`](#link)
  - [1.1. Property `EmailClick > link > anyOf > EmailLink`](#link_anyOf_i0)
    - [1.1.1. Property `EmailClick > link > anyOf > EmailLink > email`](#link_anyOf_i0_email)
  - [1.2. Property `EmailClick > link > anyOf > EmailSha256Link`](#link_anyOf_i1)
    - [1.2.1. Property `EmailClick > link > anyOf > EmailSha256Link > email_sha256`](#link_anyOf_i1_email_sha256)
  - [1.3. Property `EmailClick > link > anyOf > EmailMd5Link`](#link_anyOf_i2)
    - [1.3.1. Property `EmailClick > link > anyOf > EmailMd5Link > email_md5`](#link_anyOf_i2_email_md5)
  - [1.4. Property `EmailClick > link > anyOf > CustomerIdLink`](#link_anyOf_i3)
    - [1.4.1. Property `EmailClick > link > anyOf > CustomerIdLink > customer_id`](#link_anyOf_i3_customer_id)
    - [1.4.2. Property `EmailClick > link > anyOf > CustomerIdLink > system_name`](#link_anyOf_i3_system_name)
  - [1.5. Property `EmailClick > link > anyOf > MobileLink`](#link_anyOf_i4)
    - [1.5.1. Property `EmailClick > link > anyOf > MobileLink > mobile`](#link_anyOf_i4_mobile)
  - [1.6. Property `EmailClick > link > anyOf > ExternalLink`](#link_anyOf_i5)
    - [1.6.1. Property `EmailClick > link > anyOf > ExternalLink > external_id`](#link_anyOf_i5_external_id)
    - [1.6.2. Property `EmailClick > link > anyOf > ExternalLink > system_name`](#link_anyOf_i5_system_name)
  - [1.7. Property `EmailClick > link > anyOf > CustomerLink`](#link_anyOf_i6)
    - [1.7.1. Property `EmailClick > link > anyOf > CustomerLink > link_type`](#link_anyOf_i6_link_type)
    - [1.7.2. Property `EmailClick > link > anyOf > CustomerLink > link_value`](#link_anyOf_i6_link_value)
    - [1.7.3. Property `EmailClick > link > anyOf > CustomerLink > id_type`](#link_anyOf_i6_id_type)
- [2. Property `EmailClick > action_at`](#action_at)
- [3. Property `EmailClick > email_id`](#email_id)
- [4. Property `EmailClick > list`](#list)
  - [4.1. Property `EmailClick > list > id`](#list_id)
  - [4.2. Property `EmailClick > list > name`](#list_name)
- [5. Property `EmailClick > campaign_id`](#campaign_id)
- [6. Property `EmailClick > from`](#from)
  - [6.1. Property `EmailClick > from > name`](#from_name)
  - [6.2. Property `EmailClick > from > email`](#from_email)
- [7. Property `EmailClick > to`](#to)
- [8. Property `EmailClick > clicked_link`](#clicked_link)
  - [8.1. Property `EmailClick > clicked_link > name`](#clicked_link_name)
  - [8.2. Property `EmailClick > clicked_link > url`](#clicked_link_url)

**Title:** EmailClick

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** An Email Click Event object `record_type=email_click`.
These events are used to enrich profiles with attributes like “Email Click Rate” or “Click Dates”.

| Property                         | Pattern | Type        | Deprecated | Definition                     | Title/Description |
| -------------------------------- | ------- | ----------- | ---------- | ------------------------------ | ----------------- |
| + [link](#link )                 | No      | Combination | No         | -                              | Link              |
| + [action_at](#action_at )       | No      | string      | No         | -                              | Action At         |
| + [email_id](#email_id )         | No      | string      | No         | -                              | Email Id          |
| - [list](#list )                 | No      | object      | No         | In #/definitions/MarketingList | -                 |
| - [campaign_id](#campaign_id )   | No      | string      | No         | -                              | Campaign Id       |
| - [from](#from )                 | No      | object      | No         | In                             | From              |
| - [to](#to )                     | No      | object      | No         | Same as [from](#from )         | To                |
| - [clicked_link](#clicked_link ) | No      | object      | No         | In #/definitions/ClickedLink   | -                 |

## <a name="link"></a>1. Property `EmailClick > link`

**Title:** Link

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Any of(Option)                    |
| --------------------------------- |
| [EmailLink](#link_anyOf_i0)       |
| [EmailSha256Link](#link_anyOf_i1) |
| [EmailMd5Link](#link_anyOf_i2)    |
| [CustomerIdLink](#link_anyOf_i3)  |
| [MobileLink](#link_anyOf_i4)      |
| [ExternalLink](#link_anyOf_i5)    |
| [CustomerLink](#link_anyOf_i6)    |

### <a name="link_anyOf_i0"></a>1.1. Property `EmailClick > link > anyOf > EmailLink`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/EmailLink                                 |

| Property                         | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [email](#link_anyOf_i0_email ) | No      | string | No         | -          | Email             |

#### <a name="link_anyOf_i0_email"></a>1.1.1. Property `EmailClick > link > anyOf > EmailLink > email`

**Title:** Email

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Example:** 

```json
"jane@example.com"
```

| Restrictions                      |                                                                                                                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)``` [Test](https://regex101.com/?regex=%28%5E%5Ba-zA-Z0-9_.%2B-%5D%2B%40%5Ba-zA-Z0-9-%5D%2B%5C.%5Ba-zA-Z0-9-.%5D%2B%24%29&testString=%22jane%40example.com%22) |

### <a name="link_anyOf_i1"></a>1.2. Property `EmailClick > link > anyOf > EmailSha256Link`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/EmailSha256Link                           |

| Property                                       | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [email_sha256](#link_anyOf_i1_email_sha256 ) | No      | string | No         | -          | Email Sha256      |

#### <a name="link_anyOf_i1_email_sha256"></a>1.2.1. Property `EmailClick > link > anyOf > EmailSha256Link > email_sha256`

**Title:** Email Sha256

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Ensure that the email address is lowercase before hashing.

**Example:** 

```json
"8c87b489ce35cf2e2f39f80e282cb2e804932a56a213983eeeb428407d43b52d"
```

### <a name="link_anyOf_i2"></a>1.3. Property `EmailClick > link > anyOf > EmailMd5Link`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/EmailMd5Link                              |

| Property                                 | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [email_md5](#link_anyOf_i2_email_md5 ) | No      | string | No         | -          | Email Md5         |

#### <a name="link_anyOf_i2_email_md5"></a>1.3.1. Property `EmailClick > link > anyOf > EmailMd5Link > email_md5`

**Title:** Email Md5

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Ensure that the email address is lowercase before hashing.

**Example:** 

```json
"9e26471d35a78862c17e467d87cddedf"
```

### <a name="link_anyOf_i3"></a>1.4. Property `EmailClick > link > anyOf > CustomerIdLink`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/CustomerIdLink                            |

| Property                                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [customer_id](#link_anyOf_i3_customer_id ) | No      | string | No         | -          | Customer Id       |
| - [system_name](#link_anyOf_i3_system_name ) | No      | string | No         | -          | System Name       |

#### <a name="link_anyOf_i3_customer_id"></a>1.4.1. Property `EmailClick > link > anyOf > CustomerIdLink > customer_id`

**Title:** Customer Id

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A unique identifier for a customer.

**Example:** 

```json
"123456789"
```

#### <a name="link_anyOf_i3_system_name"></a>1.4.2. Property `EmailClick > link > anyOf > CustomerIdLink > system_name`

**Title:** System Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** An optional name for the system of origin.

**Example:** 

```json
"SuperPOS 2000"
```

### <a name="link_anyOf_i4"></a>1.5. Property `EmailClick > link > anyOf > MobileLink`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/MobileLink                                |

| Property                           | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [mobile](#link_anyOf_i4_mobile ) | No      | string | No         | -          | Mobile            |

#### <a name="link_anyOf_i4_mobile"></a>1.5.1. Property `EmailClick > link > anyOf > MobileLink > mobile`

**Title:** Mobile

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Formatted with the international code with no spaces or symbols.

**Example:** 

```json
"61491570006"
```

### <a name="link_anyOf_i5"></a>1.6. Property `EmailClick > link > anyOf > ExternalLink`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/ExternalLink                              |

| Property                                     | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [external_id](#link_anyOf_i5_external_id ) | No      | string | No         | -          | External Id       |
| + [system_name](#link_anyOf_i5_system_name ) | No      | string | No         | -          | System Name       |

#### <a name="link_anyOf_i5_external_id"></a>1.6.1. Property `EmailClick > link > anyOf > ExternalLink > external_id`

**Title:** External Id

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A unique identifier for a customer in an external system.

**Example:** 

```json
"123456789"
```

#### <a name="link_anyOf_i5_system_name"></a>1.6.2. Property `EmailClick > link > anyOf > ExternalLink > system_name`

**Title:** System Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A unique identifer for the external system itself.

**Example:** 

```json
"super_pos_2000"
```

### <a name="link_anyOf_i6"></a>1.7. Property `EmailClick > link > anyOf > CustomerLink`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/CustomerLink                              |

**Description:** This type of link is deprecated. Please use one of the other specific link types instead.

| Property                                   | Pattern | Type             | Deprecated | Definition                | Title/Description |
| ------------------------------------------ | ------- | ---------------- | ---------- | ------------------------- | ----------------- |
| + [link_type](#link_anyOf_i6_link_type )   | No      | enum (of string) | No         | In #/definitions/LinkType | An enumeration.   |
| + [link_value](#link_anyOf_i6_link_value ) | No      | string           | No         | -                         | Link Value        |
| - [id_type](#link_anyOf_i6_id_type )       | No      | string           | No         | -                         | Id Type           |

#### <a name="link_anyOf_i6_link_type"></a>1.7.1. Property `EmailClick > link > anyOf > CustomerLink > link_type`

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `enum (of string)`     |
| **Required**   | Yes                    |
| **Defined in** | #/definitions/LinkType |

**Description:** An enumeration.

Must be one of:
* "email"
* "email_sha256"
* "customer_id"
* "mobile"
* "engage.id"
* "external_id"
* "email_md5"

#### <a name="link_anyOf_i6_link_value"></a>1.7.2. Property `EmailClick > link > anyOf > CustomerLink > link_value`

**Title:** Link Value

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

#### <a name="link_anyOf_i6_id_type"></a>1.7.3. Property `EmailClick > link > anyOf > CustomerLink > id_type`

**Title:** Id Type

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"default"` |

## <a name="action_at"></a>2. Property `EmailClick > action_at`

**Title:** Action At

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | Yes         |
| **Format**   | `date-time` |

## <a name="email_id"></a>3. Property `EmailClick > email_id`

**Title:** Email Id

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A unique identifier for an individual email event.

**Example:** 

```json
"send-job-a7e23-jane-doe"
```

## <a name="list"></a>4. Property `EmailClick > list`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/MarketingList                                               |

| Property              | Pattern | Type   | Deprecated | Definition | Title/Description |
| --------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [id](#list_id )     | No      | string | No         | -          | Id                |
| + [name](#list_name ) | No      | string | No         | -          | Name              |

### <a name="list_id"></a>4.1. Property `EmailClick > list > id`

**Title:** Id

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Example:** 

```json
"7bff7a..."
```

### <a name="list_name"></a>4.2. Property `EmailClick > list > name`

**Title:** Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Examples:** 

```json
"All Customers List"
```

```json
"Lapsed Customers"
```

## <a name="campaign_id"></a>5. Property `EmailClick > campaign_id`

**Title:** Campaign Id

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Campaign Identifier or Name.

**Example:** 

```json
"Black friday Menswear Teaser Aug 2020"
```

## <a name="from"></a>6. Property `EmailClick > from`

**Title:** From

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            |                                                                           |

**Description:** Sender Details

| Property                | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [name](#from_name )   | No      | string | No         | -          | Name              |
| + [email](#from_email ) | No      | string | No         | -          | Email             |

### <a name="from_name"></a>6.1. Property `EmailClick > from > name`

**Title:** Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"Jane Doe"
```

### <a name="from_email"></a>6.2. Property `EmailClick > from > email`

**Title:** Email

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Example:** 

```json
"jane@example.com"
```

| Restrictions                      |                                                                                                                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)``` [Test](https://regex101.com/?regex=%28%5E%5Ba-zA-Z0-9_.%2B-%5D%2B%40%5Ba-zA-Z0-9-%5D%2B%5C.%5Ba-zA-Z0-9-.%5D%2B%24%29&testString=%22jane%40example.com%22) |

## <a name="to"></a>7. Property `EmailClick > to`

**Title:** To

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [from](#from)                                                             |

**Description:** Recipient Details

## <a name="clicked_link"></a>8. Property `EmailClick > clicked_link`

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/ClickedLink                                                 |

| Property                      | Pattern | Type   | Deprecated | Definition | Title/Description |
| ----------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [name](#clicked_link_name ) | No      | string | No         | -          | Name              |
| - [url](#clicked_link_url )   | No      | string | No         | -          | Url               |

### <a name="clicked_link_name"></a>8.1. Property `EmailClick > clicked_link > name`

**Title:** Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The plain text name of the link.

### <a name="clicked_link_url"></a>8.2. Property `EmailClick > clicked_link > url`

**Title:** Url

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The URL link.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
