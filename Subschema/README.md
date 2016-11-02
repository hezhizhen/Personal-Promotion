# Subschema

[An App shows how to use Subschema](http://subschema.github.io/subschema/#/?_k=9iv2ws)

[Github Page](https://github.com/subschema/subschema)

## Install

```bash
$ npm install subschema
```

## Usage

```json
import React, {Component} from 'react';
import {Form} from 'Subschema';
```

## Built In Types

### Autocomplete

### Checkbox

### Checkboxes

### Content

### Date

### DateTime

### Hidden

### List

### Mixed

### Number

### Object

### Password

### Radio

### Restricted

### Select

### Text

### TextArea

## Example

```json
<Form
    action='/submit/path'
    method='POST'
    schema={{
    schema: {
    title: {
        type: 'Select',
        options: ['Mr', 'Mrs', 'Ms']
    },
    name: 'Text',
    email: {
    validators: ['required', 'email']
    },
    birthday: 'Date',
    password: 'Password',
    address: {
        type: 'Object',
        subSchema: {
        'street': {
            type: 'Text',
            validators: ['required']
        },
        city: 'Text',
        zip:{
            type: 'Text',
            validators: ['required', /\d{5}(-\d{4})?/]
        }
        }
    },
    notes: {
        type: 'List',
        itemType: 'Text'
    }
    },
    fieldsets: [
    {
        legend: 'Name',
        fields: ['title', 'email', 'name', 'password']
    },
    {
        legend: 'Address',
        fields: ['address.street', 'address.city', 'address.zip']
    }
    ]
    }}
}/>
```

## Loaders

for new types, validators, templates and schemas; call the corresponding add method

### schema loader

reuse an existing schema: register your schema and reference it as a string in anywhere an object takes a subSchema or a schema

```json
var loaded = loader.addSchema({
Address: {
    address: 'Text',
    city: 'Text',
    state: {
        type: 'Select',
        options: ['CA', 'FL', 'VA', 'IL']
    },
    zipCode: {
        type: 'Text',
        dataType: 'number'
    }
},
Contact: {
schema: {
    name: 'Text',
    primary: {
        type: 'ToggleObject',
        subSchema: 'Address',
        template: 'simpleTemplate'
    },
    otherAddress: {
        canEdit: true,
        canReorder: true,
        canDelete: true,
        canAdd: true,
        type: 'List',
        labelKey: 'address',
        itemType: {
            type: 'Object',
            subSchema: 'Address'
        }
    }
},
fields: ['name', 'primary', 'otherAddress']
}
});

<Form schema="Contact"/>
```

## Events

events can be registered via the `ValueManager`; you can subscribe to a path, a part of a path or all events of a type

