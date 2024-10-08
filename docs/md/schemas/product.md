# ProductRecord

- [1. Property `ProductRecord > product_id`](#product_id)
- [2. Property `ProductRecord > sku`](#sku)
- [3. Property `ProductRecord > upc`](#upc)
- [4. Property `ProductRecord > product_reference_type`](#product_reference_type)
- [5. Property `ProductRecord > name`](#name)
- [6. Property `ProductRecord > description`](#description)
- [7. Property `ProductRecord > brand`](#brand)
- [8. Property `ProductRecord > size`](#size)
- [9. Property `ProductRecord > color`](#color)
- [10. Property `ProductRecord > price`](#price)
- [11. Property `ProductRecord > options`](#options)
  - [11.1. Property `ProductRecord > options > additionalProperties`](#options_additionalProperties)
    - [11.1.1. ProductRecord > options > additionalProperties > additionalProperties items](#autogenerated_heading_2)
- [12. Property `ProductRecord > url`](#url)
- [13. Property `ProductRecord > images`](#images)
  - [13.1. ProductRecord > images > images items](#autogenerated_heading_3)
- [14. Property `ProductRecord > availability`](#availability)
  - [14.1. Property `ProductRecord > availability > available`](#availability_available)
  - [14.2. Property `ProductRecord > availability > channels_availability`](#availability_channels_availability)
    - [14.2.1. ProductRecord > availability > channels_availability > ProductChannelAvailability](#autogenerated_heading_4)
      - [14.2.1.1. Property `ProductRecord > availability > channels_availability > ProductChannelAvailability > type`](#availability_channels_availability_items_type)
      - [14.2.1.2. Property `ProductRecord > availability > channels_availability > ProductChannelAvailability > available`](#availability_channels_availability_items_available)
      - [14.2.1.3. Property `ProductRecord > availability > channels_availability > ProductChannelAvailability > published_at`](#availability_channels_availability_items_published_at)
      - [14.2.1.4. Property `ProductRecord > availability > channels_availability > ProductChannelAvailability > unpublished_at`](#availability_channels_availability_items_unpublished_at)
- [15. Property `ProductRecord > inventory`](#inventory)
  - [15.1. Property `ProductRecord > inventory > id`](#inventory_id)
  - [15.2. Property `ProductRecord > inventory > source`](#inventory_source)
  - [15.3. Property `ProductRecord > inventory > quantity`](#inventory_quantity)
  - [15.4. Property `ProductRecord > inventory > cost`](#inventory_cost)
  - [15.5. Property `ProductRecord > inventory > backorder_allowed`](#inventory_backorder_allowed)
  - [15.6. Property `ProductRecord > inventory > tracked`](#inventory_tracked)
  - [15.7. Property `ProductRecord > inventory > updated_at`](#inventory_updated_at)

**Title:** ProductRecord

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

**Description:** A product object `record_type=product`.
Product records are used to represent the current and historical products offered by your brand, including your product taxonomy.
The field referenced in `product_reference_type` should be unique and used in purchase and return events.

| Property                                             | Pattern | Type             | Deprecated | Definition | Title/Description      |
| ---------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ---------------------- |
| - [product_id](#product_id )                         | No      | string           | No         | -          | Product ID             |
| - [sku](#sku )                                       | No      | string           | No         | -          | SKU                    |
| - [upc](#upc )                                       | No      | string           | No         | -          | UPC                    |
| - [product_reference_type](#product_reference_type ) | No      | enum (of string) | No         | In         | Product Reference Type |
| - [name](#name )                                     | No      | string           | No         | -          | Product Name           |
| - [description](#description )                       | No      | string           | No         | -          | Description            |
| - [brand](#brand )                                   | No      | string           | No         | -          | Brand Name             |
| - [size](#size )                                     | No      | string           | No         | -          | Size                   |
| - [color](#color )                                   | No      | string           | No         | -          | Color                  |
| - [price](#price )                                   | No      | number           | No         | -          | Price                  |
| - [options](#options )                               | No      | object           | No         | -          | Categories             |
| - [url](#url )                                       | No      | string           | No         | -          | Product URL            |
| - [images](#images )                                 | No      | array of string  | No         | -          | Image URLs             |
| - [availability](#availability )                     | No      | object           | No         | In         | Product Availability   |
| - [inventory](#inventory )                           | No      | object           | No         | In         | Product Inventory      |

## <a name="product_id"></a>1. Property `ProductRecord > product_id`

**Title:** Product ID

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Unique product_id. Required if `product_id` is used as the product identifier in `product_reference_type`.

**Example:** 

```json
"b7c901..."
```

## <a name="sku"></a>2. Property `ProductRecord > sku`

**Title:** SKU

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Unique SKU. Required if `sku` is used as a product identifier in `product_reference_type`.

**Example:** 

```json
"ac6674..."
```

## <a name="upc"></a>3. Property `ProductRecord > upc`

**Title:** UPC

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Unique UPC. Required if `upc` is used as a product identifier in `product_reference_type`.

**Example:** 

```json
"ce6378..."
```

## <a name="product_reference_type"></a>4. Property `ProductRecord > product_reference_type`

**Title:** Product Reference Type

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | No                 |
| **Default**    | `"product_id"`     |
| **Defined in** |                    |

**Description:** Which field is used to identify the product entity. A value must be provided in the specified field.

Must be one of:
* "sku"
* "upc"
* "product_id"

## <a name="name"></a>5. Property `ProductRecord > name`

**Title:** Product Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"Organic Sawyer Rib Crew Knit"
```

## <a name="description"></a>6. Property `ProductRecord > description`

**Title:** Description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"Whether your look is clean and casual or sharp and sophisticated, Staple Superior has what you need to achieve that effortlessly cool style."
```

## <a name="brand"></a>7. Property `ProductRecord > brand`

**Title:** Brand Name

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"Sawyer"
```

## <a name="size"></a>8. Property `ProductRecord > size`

**Title:** Size

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"L"
```

## <a name="color"></a>9. Property `ProductRecord > color`

**Title:** Color

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Example:** 

```json
"Navy"
```

## <a name="price"></a>10. Property `ProductRecord > price`

**Title:** Price

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Example:** 

```json
89.0
```

## <a name="options"></a>11. Property `ProductRecord > options`

**Title:** Categories

|                           |                                                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                          |
| **Required**              | No                                                                                                                |
| **Additional properties** | [[Should-conform]](#options_additionalProperties "Each additional property must conform to the following schema") |

**Description:** Key value pairs of options that define the product, such as departments, categories, styles, etc.

**Example:** 

```json
{
    "department": [
        "menswear"
    ],
    "category": [
        "outerwear"
    ],
    "subcategory": [
        "knits",
        "wool"
    ]
}
```

| Property                             | Pattern | Type            | Deprecated | Definition | Title/Description |
| ------------------------------------ | ------- | --------------- | ---------- | ---------- | ----------------- |
| - [](#options_additionalProperties ) | No      | array of string | No         | -          | -                 |

### <a name="options_additionalProperties"></a>11.1. Property `ProductRecord > options > additionalProperties`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                   | Description |
| ----------------------------------------------------------------- | ----------- |
| [additionalProperties items](#options_additionalProperties_items) | -           |

#### <a name="autogenerated_heading_2"></a>11.1.1. ProductRecord > options > additionalProperties > additionalProperties items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="url"></a>12. Property `ProductRecord > url`

**Title:** Product URL

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** A URL to the product listed on the public internet - i.e., an ecommerce link.

**Example:** 

```json
"https://fake.com/menswear/sawyer-rib-crew-knit"
```

## <a name="images"></a>13. Property `ProductRecord > images`

**Title:** Image URLs

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |

**Description:** An array of Product Image URLs listed on the public internet.

**Example:** 

```json
[
    "https://fake.com/images/menswear/sawyer-rib-crew-knit.jpg"
]
```

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [images items](#images_items)   | -           |

### <a name="autogenerated_heading_3"></a>13.1. ProductRecord > images > images items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `uri`    |

| Restrictions   |      |
| -------------- | ---- |
| **Min length** | 1    |
| **Max length** | 2083 |

## <a name="availability"></a>14. Property `ProductRecord > availability`

**Title:** Product Availability

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            |                                                                           |

**Description:** The availability status of the product.

| Property                                                        | Pattern | Type    | Deprecated | Definition | Title/Description     |
| --------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | --------------------- |
| + [available](#availability_available )                         | No      | boolean | No         | -          | Available             |
| - [channels_availability](#availability_channels_availability ) | No      | array   | No         | -          | Channels Availability |

### <a name="availability_available"></a>14.1. Property `ProductRecord > availability > available`

**Title:** Available

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | Yes       |

**Description:** A product is available when it is suitable for sale in any channel, or can be promoted in marketing communications.

**Example:** 

```json
false
```

### <a name="availability_channels_availability"></a>14.2. Property `ProductRecord > availability > channels_availability`

**Title:** Channels Availability

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** A list of channel specific availability statuses.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                         | Description |
| ----------------------------------------------------------------------- | ----------- |
| [ProductChannelAvailability](#availability_channels_availability_items) | -           |

#### <a name="autogenerated_heading_4"></a>14.2.1. ProductRecord > availability > channels_availability > ProductChannelAvailability

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/ProductChannelAvailability                                  |

| Property                                                                      | Pattern | Type             | Deprecated | Definition | Title/Description                                      |
| ----------------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ------------------------------------------------------ |
| + [type](#availability_channels_availability_items_type )                     | No      | enum (of string) | No         | In         | The channel which this availability record relates to. |
| + [available](#availability_channels_availability_items_available )           | No      | boolean          | No         | -          | Available                                              |
| - [published_at](#availability_channels_availability_items_published_at )     | No      | string           | No         | -          | Published At                                           |
| - [unpublished_at](#availability_channels_availability_items_unpublished_at ) | No      | string           | No         | -          | Unpublished At                                         |

##### <a name="availability_channels_availability_items_type"></a>14.2.1.1. Property `ProductRecord > availability > channels_availability > ProductChannelAvailability > type`

|                |                    |
| -------------- | ------------------ |
| **Type**       | `enum (of string)` |
| **Required**   | Yes                |
| **Defined in** |                    |

**Description:** The channel which this availability record relates to.

**Example:** 

```json
"ecommerce"
```

**Example:** 

```json
"ecommerce"
```

Must be one of:
* "physical"
* "ecommerce"

##### <a name="availability_channels_availability_items_available"></a>14.2.1.2. Property `ProductRecord > availability > channels_availability > ProductChannelAvailability > available`

**Title:** Available

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | Yes       |

**Description:** Is the product available for purchase via this specific channel?

**Example:** 

```json
false
```

##### <a name="availability_channels_availability_items_published_at"></a>14.2.1.3. Property `ProductRecord > availability > channels_availability > ProductChannelAvailability > published_at`

**Title:** Published At

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Format**   | `date-time` |

**Description:** An ISO8601 datetime string for when the product was published, or is going to be published to this channel.

**Example:** 

```json
"2024-01-01T00:00:00Z"
```

##### <a name="availability_channels_availability_items_unpublished_at"></a>14.2.1.4. Property `ProductRecord > availability > channels_availability > ProductChannelAvailability > unpublished_at`

**Title:** Unpublished At

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Format**   | `date-time` |

**Description:** An ISO8601 datetime string for when the product was unpublished, or is going to be unpublished to this channel.

**Example:** 

```json
"2025-01-01T00:00:00Z"
```

## <a name="inventory"></a>15. Property `ProductRecord > inventory`

**Title:** Product Inventory

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Defined in**            |                                                                           |

**Description:** The inventory status of the product.

| Property                                             | Pattern | Type    | Deprecated | Definition | Title/Description |
| ---------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [id](#inventory_id )                               | No      | string  | No         | -          | Id                |
| - [source](#inventory_source )                       | No      | string  | No         | -          | Source            |
| - [quantity](#inventory_quantity )                   | No      | integer | No         | -          | Quantity          |
| - [cost](#inventory_cost )                           | No      | number  | No         | -          | Cost              |
| - [backorder_allowed](#inventory_backorder_allowed ) | No      | boolean | No         | -          | Backorder Allowed |
| - [tracked](#inventory_tracked )                     | No      | boolean | No         | -          | Tracked           |
| - [updated_at](#inventory_updated_at )               | No      | string  | No         | -          | Updated At        |

### <a name="inventory_id"></a>15.1. Property `ProductRecord > inventory > id`

**Title:** Id

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Identifier of product in the inventory system.

**Example:** 

```json
"lzx0h1..."
```

### <a name="inventory_source"></a>15.2. Property `ProductRecord > inventory > source`

**Title:** Source

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Source of inventory product data, e.g. Shopify, Magento..

**Example:** 

```json
"Shopify"
```

### <a name="inventory_quantity"></a>15.3. Property `ProductRecord > inventory > quantity`

**Title:** Quantity

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** Total number of remaining product units.

**Example:** 

```json
99
```

### <a name="inventory_cost"></a>15.4. Property `ProductRecord > inventory > cost`

**Title:** Cost

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** Total expenditure incurred to produce, store and sell one unit of product.

**Example:** 

```json
50.0
```

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

### <a name="inventory_backorder_allowed"></a>15.5. Property `ProductRecord > inventory > backorder_allowed`

**Title:** Backorder Allowed

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

**Description:** Can the product item be ordered when it's out of stock?

**Example:** 

```json
false
```

### <a name="inventory_tracked"></a>15.6. Property `ProductRecord > inventory > tracked`

**Title:** Tracked

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

**Description:** Is the product quantity being tracked?

**Example:** 

```json
false
```

### <a name="inventory_updated_at"></a>15.7. Property `ProductRecord > inventory > updated_at`

**Title:** Updated At

|              |             |
| ------------ | ----------- |
| **Type**     | `string`    |
| **Required** | No          |
| **Format**   | `date-time` |

**Description:** An ISO8601 datetime string for when the product inventory status was last updated.

**Example:** 

```json
"2024-01-01T00:00:00Z"
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
