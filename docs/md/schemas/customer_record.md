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
- [16. Property `CustomerRecord > employee_flag`](#employee_flag)
- [17. Property `CustomerRecord > customer_type`](#customer_type)
- [18. Property `CustomerRecord > address_1`](#address_1)
- [19. Property `CustomerRecord > address_2`](#address_2)

**Title:** CustomerRecord

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                           | Pattern | Type        | Deprecated | Definition | Title/Description |
| ---------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| + [link](#link )                   | No      | Combination | No         | -          | Link              |
| - [email](#email )                 | No      | string      | No         | -          | Email             |
| - [email_sha256](#email_sha256 )   | No      | string      | No         | -          | Email Sha256      |
| - [mobile](#mobile )               | No      | string      | No         | -          | Mobile            |
| - [customer_id](#customer_id )     | No      | string      | No         | -          | Customer Id       |
| - [custom_fields](#custom_fields ) | No      | object      | No         | -          | Custom Fields     |
| - [first_name](#first_name )       | No      | string      | No         | -          | First Name        |
| - [last_name](#last_name )         | No      | string      | No         | -          | Last Name         |
| - [gender](#gender )               | No      | string      | No         | -          | Gender            |
| - [date_of_birth](#date_of_birth ) | No      | string      | No         | -          | Date Of Birth     |
| - [country](#country )             | No      | string      | No         | -          | Country           |
| - [state](#state )                 | No      | string      | No         | -          | State             |
| - [city](#city )                   | No      | string      | No         | -          | City              |
| - [postcode](#postcode )           | No      | string      | No         | -          | Postcode          |
| - [zip](#zip )                     | No      | string      | No         | -          | Zip               |
| - [employee_flag](#employee_flag ) | No      | boolean     | No         | -          | Employee Flag     |
| - [customer_type](#customer_type ) | No      | string      | No         | -          | Customer Type     |
| - [address_1](#address_1 )         | No      | string      | No         | -          | Address 1         |
| - [address_2](#address_2 )         | No      | string      | No         | -          | Address 2         |

## <a name="link"></a>1. Property `CustomerRecord > link`

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

#### <a name="link_anyOf_i3_system_name"></a>1.4.2. Property `CustomerRecord > link > anyOf > CustomerIdLink > system_name`

**Title:** System Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

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

#### <a name="link_anyOf_i5_system_name"></a>1.6.2. Property `CustomerRecord > link > anyOf > ExternalLink > system_name`

**Title:** System Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

### <a name="link_anyOf_i6"></a>1.7. Property `CustomerRecord > link > anyOf > CustomerLink`

|                           |                                                         |
| ------------------------- | ------------------------------------------------------- |
| **Type**                  | `object`                                                |
| **Required**              | No                                                      |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
| **Defined in**            | #/definitions/CustomerLink                              |

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

**Title:** Email

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="email_sha256"></a>3. Property `CustomerRecord > email_sha256`

**Title:** Email Sha256

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="mobile"></a>4. Property `CustomerRecord > mobile`

**Title:** Mobile

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="customer_id"></a>5. Property `CustomerRecord > customer_id`

**Title:** Customer Id

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="custom_fields"></a>6. Property `CustomerRecord > custom_fields`

**Title:** Custom Fields

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

## <a name="first_name"></a>7. Property `CustomerRecord > first_name`

**Title:** First Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="last_name"></a>8. Property `CustomerRecord > last_name`

**Title:** Last Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="gender"></a>9. Property `CustomerRecord > gender`

**Title:** Gender

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="date_of_birth"></a>10. Property `CustomerRecord > date_of_birth`

**Title:** Date Of Birth

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `date`   |

## <a name="country"></a>11. Property `CustomerRecord > country`

**Title:** Country

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="state"></a>12. Property `CustomerRecord > state`

**Title:** State

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="city"></a>13. Property `CustomerRecord > city`

**Title:** City

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="postcode"></a>14. Property `CustomerRecord > postcode`

**Title:** Postcode

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="zip"></a>15. Property `CustomerRecord > zip`

**Title:** Zip

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="employee_flag"></a>16. Property `CustomerRecord > employee_flag`

**Title:** Employee Flag

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

## <a name="customer_type"></a>17. Property `CustomerRecord > customer_type`

**Title:** Customer Type

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="address_1"></a>18. Property `CustomerRecord > address_1`

**Title:** Address 1

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="address_2"></a>19. Property `CustomerRecord > address_2`

**Title:** Address 2

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2023-07-26 at 00:41:56 +0000
