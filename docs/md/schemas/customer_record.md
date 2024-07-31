# CustomerRecord

- [1. Property `CustomerRecord > link`](#link)
  - [1.1. Property `CustomerRecord > link > anyOf > EmailLink`](#link_anyOf_i0)
    - [1.1.1. Property `CustomerRecord > link > anyOf > EmailLink > email`](#link_anyOf_i0_email)
  - [1.2. Property `CustomerRecord > link > anyOf > EmailSha256Link`](#link_anyOf_i1)
    - [1.2.1. Property `CustomerRecord > link > anyOf > EmailSha256Link > email_sha256`](#link_anyOf_i1_email_sha256)
  - [1.3. Property `CustomerRecord > link > anyOf > EmailMd5Link`](#link_anyOf_i2)
    - [1.3.1. Property `CustomerRecord > link > anyOf > EmailMd5Link > email_md5`](#link_anyOf_i2_email_md5)
  - [1.4. Property `CustomerRecord > link > anyOf > CustomerIdLink`](#link_anyOf_i3)
    - [1.4.1. Property `CustomerRecord > link > anyOf > CustomerIdLink > customer_id`](#link_anyOf_i3_customer_id)
    - [1.4.2. Property `CustomerRecord > link > anyOf > CustomerIdLink > system_name`](#link_anyOf_i3_system_name)
  - [1.5. Property `CustomerRecord > link > anyOf > MobileLink`](#link_anyOf_i4)
    - [1.5.1. Property `CustomerRecord > link > anyOf > MobileLink > mobile`](#link_anyOf_i4_mobile)
  - [1.6. Property `CustomerRecord > link > anyOf > ExternalLink`](#link_anyOf_i5)
    - [1.6.1. Property `CustomerRecord > link > anyOf > ExternalLink > external_id`](#link_anyOf_i5_external_id)
    - [1.6.2. Property `CustomerRecord > link > anyOf > ExternalLink > system_name`](#link_anyOf_i5_system_name)
  - [1.7. Property `CustomerRecord > link > anyOf > CustomerLink`](#link_anyOf_i6)
    - [1.7.1. Property `CustomerRecord > link > anyOf > CustomerLink > link_type`](#link_anyOf_i6_link_type)
    - [1.7.2. Property `CustomerRecord > link > anyOf > CustomerLink > link_value`](#link_anyOf_i6_link_value)
    - [1.7.3. Property `CustomerRecord > link > anyOf > CustomerLink > id_type`](#link_anyOf_i6_id_type)
- [2. Property `CustomerRecord > email`](#email)
- [3. Property `CustomerRecord > email_sha256`](#email_sha256)
- [4. Property `CustomerRecord > mobile`](#mobile)
- [5. Property `CustomerRecord > customer_id`](#customer_id)
- [6. Property `CustomerRecord > custom_fields`](#custom_fields)
- [7. Property `CustomerRecord > first_name`](#first_name)
- [8. Property `CustomerRecord > last_name`](#last_name)
- [9. Property `CustomerRecord > gender`](#gender)
- [10. Property `CustomerRecord > date_of_birth`](#date_of_birth)
- [11. Property `CustomerRecord > country`](#country)
- [12. Property `CustomerRecord > state`](#state)
- [13. Property `CustomerRecord > city`](#city)
- [14. Property `CustomerRecord > postcode`](#postcode)
- [15. Property `CustomerRecord > zip`](#zip)
- [16. Property `CustomerRecord > address_1`](#address_1)
- [17. Property `CustomerRecord > address_2`](#address_2)
- [18. Property `CustomerRecord > employee_flag`](#employee_flag)
- [19. Property `CustomerRecord > customer_type`](#customer_type)

**Title:** CustomerRecord

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** A customer object `record_type=customer_record`.
Represents customer information, such as traditional CRM entries, user account information, and so on, in the CDXP.
The Lexer CDXP will resolve related customer records into one profile, creating a single representation of a profile based on the rules configured within the Hub.

| Property                           | Pattern | Type        | Deprecated | Definition | Title/Description   |
| ---------------------------------- | ------- | ----------- | ---------- | ---------- | ------------------- |
| + [link](#link )                   | No      | Combination | No         | -          | Link                |
| - [email](#email )                 | No      | string      | No         | -          | Email Address       |
| - [email_sha256](#email_sha256 )   | No      | string      | No         | -          | Email Sha256        |
| - [mobile](#mobile )               | No      | string      | No         | -          | Mobile Phone Number |
| - [customer_id](#customer_id )     | No      | string      | No         | -          | Customer Id         |
| - [custom_fields](#custom_fields ) | No      | object      | No         | -          | Custom Fields       |
| - [first_name](#first_name )       | No      | string      | No         | -          | First Name          |
| - [last_name](#last_name )         | No      | string      | No         | -          | Last Name           |
| - [gender](#gender )               | No      | string      | No         | -          | Gender              |
| - [date_of_birth](#date_of_birth ) | No      | string      | No         | -          | Date Of Birth       |
| - [country](#country )             | No      | string      | No         | -          | Country             |
| - [state](#state )                 | No      | string      | No         | -          | State               |
| - [city](#city )                   | No      | string      | No         | -          | City                |
| - [postcode](#postcode )           | No      | string      | No         | -          | Postcode            |
| - [zip](#zip )                     | No      | string      | No         | -          | Zip                 |
| - [address_1](#address_1 )         | No      | string      | No         | -          | Address 1           |
| - [address_2](#address_2 )         | No      | string      | No         | -          | Address 2           |
| - [employee_flag](#employee_flag ) | No      | boolean     | No         | -          | Employee Flag       |
| - [customer_type](#customer_type ) | No      | string      | No         | -          | Customer Type       |

## <a name="link"></a>1. Property `CustomerRecord > link`

**Title:** Link

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                               |
| **Required**              | Yes                                                                       |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** A value that uniquely identifies the customer, i.e. the primary key for customer records.

**Examples:** 

```json
{
    "email": "jane@example.com"
}
```

```json
{
    "customer_id": "C-2819279",
    "system_name": "super_pos_2000"
}
```

```json
{
    "mobile": "61491570006"
}
```

| Any of(Option)                    |
| --------------------------------- |
| [EmailLink](#link_anyOf_i0)       |
| [EmailSha256Link](#link_anyOf_i1) |
| [EmailMd5Link](#link_anyOf_i2)    |
| [CustomerIdLink](#link_anyOf_i3)  |
| [MobileLink](#link_anyOf_i4)      |
| [ExternalLink](#link_anyOf_i5)    |
| [CustomerLink](#link_anyOf_i6)    |

### <a name="link_anyOf_i0"></a>1.1. Property `CustomerRecord > link > anyOf > EmailLink`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/EmailLink                                 |

| Property                         | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [email](#link_anyOf_i0_email ) | No      | string | No         | -          | Email             |

#### <a name="link_anyOf_i0_email"></a>1.1.1. Property `CustomerRecord > link > anyOf > EmailLink > email`

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

### <a name="link_anyOf_i1"></a>1.2. Property `CustomerRecord > link > anyOf > EmailSha256Link`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/EmailSha256Link                           |

| Property                                       | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [email_sha256](#link_anyOf_i1_email_sha256 ) | No      | string | No         | -          | Email Sha256      |

#### <a name="link_anyOf_i1_email_sha256"></a>1.2.1. Property `CustomerRecord > link > anyOf > EmailSha256Link > email_sha256`

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

### <a name="link_anyOf_i2"></a>1.3. Property `CustomerRecord > link > anyOf > EmailMd5Link`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/EmailMd5Link                              |

| Property                                 | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [email_md5](#link_anyOf_i2_email_md5 ) | No      | string | No         | -          | Email Md5         |

#### <a name="link_anyOf_i2_email_md5"></a>1.3.1. Property `CustomerRecord > link > anyOf > EmailMd5Link > email_md5`

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

### <a name="link_anyOf_i3"></a>1.4. Property `CustomerRecord > link > anyOf > CustomerIdLink`

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

#### <a name="link_anyOf_i3_customer_id"></a>1.4.1. Property `CustomerRecord > link > anyOf > CustomerIdLink > customer_id`

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

#### <a name="link_anyOf_i3_system_name"></a>1.4.2. Property `CustomerRecord > link > anyOf > CustomerIdLink > system_name`

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

### <a name="link_anyOf_i4"></a>1.5. Property `CustomerRecord > link > anyOf > MobileLink`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/MobileLink                                |

| Property                           | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [mobile](#link_anyOf_i4_mobile ) | No      | string | No         | -          | Mobile            |

#### <a name="link_anyOf_i4_mobile"></a>1.5.1. Property `CustomerRecord > link > anyOf > MobileLink > mobile`

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

### <a name="link_anyOf_i5"></a>1.6. Property `CustomerRecord > link > anyOf > ExternalLink`

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

#### <a name="link_anyOf_i5_external_id"></a>1.6.1. Property `CustomerRecord > link > anyOf > ExternalLink > external_id`

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

#### <a name="link_anyOf_i5_system_name"></a>1.6.2. Property `CustomerRecord > link > anyOf > ExternalLink > system_name`

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

### <a name="link_anyOf_i6"></a>1.7. Property `CustomerRecord > link > anyOf > CustomerLink`

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

#### <a name="link_anyOf_i6_link_type"></a>1.7.1. Property `CustomerRecord > link > anyOf > CustomerLink > link_type`

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

#### <a name="link_anyOf_i6_link_value"></a>1.7.2. Property `CustomerRecord > link > anyOf > CustomerLink > link_value`

**Title:** Link Value

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |   |
| -------------- | - |
| **Min length** | 1 |

#### <a name="link_anyOf_i6_id_type"></a>1.7.3. Property `CustomerRecord > link > anyOf > CustomerLink > id_type`

**Title:** Id Type

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Default**  | `"default"` |

## <a name="email"></a>2. Property `CustomerRecord > email`

**Title:** Email Address

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `email`  |

**Description:** Raw email address. This will not be used for linking, but is available for use as an attribute in the CDE

**Example:** 

```json
"jane@fake.com"
```

| Restrictions                      |                                                                                                                                                                                                                  |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Must match regular expression** | ```(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)``` [Test](https://regex101.com/?regex=%28%5E%5Ba-zA-Z0-9_.%2B-%5D%2B%40%5Ba-zA-Z0-9-%5D%2B%5C.%5Ba-zA-Z0-9-.%5D%2B%24%29&testString=%22jane%40fake.com%22) |

## <a name="email_sha256"></a>3. Property `CustomerRecord > email_sha256`

**Title:** Email Sha256

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A hexadecimal string representing SHA 256 sum of a lowercased email address with trimmed whitespace. This will not be used for linking, but is available for use as an attribute in the CDE

**Example:** 

```json
"8b1885..."
```

## <a name="mobile"></a>4. Property `CustomerRecord > mobile`

**Title:** Mobile Phone Number

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A mobile phone number including country code, no whitespace or punctuation. This will not be used for linking, but is available for use as an attribute in the CDE

**Example:** 

```json
"61491570006"
```

## <a name="customer_id"></a>5. Property `CustomerRecord > customer_id`

**Title:** Customer Id

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"b6ef3b..."
```

## <a name="custom_fields"></a>6. Property `CustomerRecord > custom_fields`

**Title:** Custom Fields

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** Custom Fields. Properties are open, but a dataset may be configured to accept only particular fields to facilitate automated processing in the Lexer CDP.

**Example:** 

```json
{
    "churn_risk": 0.291,
    "loyalty_status": "platinum"
}
```

## <a name="first_name"></a>7. Property `CustomerRecord > first_name`

**Title:** First Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"Jane"
```

## <a name="last_name"></a>8. Property `CustomerRecord > last_name`

**Title:** Last Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"Doe"
```

## <a name="gender"></a>9. Property `CustomerRecord > gender`

**Title:** Gender

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"Female"
```

## <a name="date_of_birth"></a>10. Property `CustomerRecord > date_of_birth`

**Title:** Date Of Birth

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `date`   |

**Description:** An ISO8601 date string referring to the customer's date of birth

**Example:** 

```json
"2023-07-28"
```

## <a name="country"></a>11. Property `CustomerRecord > country`

**Title:** Country

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"Australia"
```

## <a name="state"></a>12. Property `CustomerRecord > state`

**Title:** State

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"Victoria"
```

## <a name="city"></a>13. Property `CustomerRecord > city`

**Title:** City

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"St Kilda"
```

## <a name="postcode"></a>14. Property `CustomerRecord > postcode`

**Title:** Postcode

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"3182"
```

## <a name="zip"></a>15. Property `CustomerRecord > zip`

**Title:** Zip

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"90291"
```

## <a name="address_1"></a>16. Property `CustomerRecord > address_1`

**Title:** Address 1

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"Inkerman St"
```

## <a name="address_2"></a>17. Property `CustomerRecord > address_2`

**Title:** Address 2

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="employee_flag"></a>18. Property `CustomerRecord > employee_flag`

**Title:** Employee Flag

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

**Description:** `true` if this customer is an employee of the business. Useful for suppressing them from messages, ad campaigns, and excluding them from searches.

**Example:** 

```json
false
```

## <a name="customer_type"></a>19. Property `CustomerRecord > customer_type`

**Title:** Customer Type

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"VIP"
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
