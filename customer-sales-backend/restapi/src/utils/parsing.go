package utils

import (
	"errors"
	"fmt"
	"reflect"
)

type ReflectParserUtils struct{}

func (p *ReflectParserUtils) GetReflectValueObject(obj interface{}) reflect.Value {
	return reflect.ValueOf(obj)
}

func (p *ReflectParserUtils) GetFieldValue(reflectObj reflect.Value, fieldName string) (any, error) {
	fieldValue := reflectObj.FieldByName(fieldName)

	if !fieldValue.IsValid() {
		return nil, fmt.Errorf("field %s does not exist in payload", fieldName)
	}

	var value any
	switch fieldValue.Kind() {
	case reflect.String:
		value = fieldValue.String()
	case reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64:
		value = fieldValue.Int()
	case reflect.Uint, reflect.Uint8, reflect.Uint16, reflect.Uint32, reflect.Uint64:
		value = fieldValue.Uint()
	case reflect.Float32, reflect.Float64:
		value = fieldValue.Float()
	case reflect.Bool:
		value = fieldValue.Bool()
	case reflect.Struct:
		if fieldValue.Type().String() == "time.Time" {
			value = fieldValue.Interface()
		} else {
			return nil, fmt.Errorf("unsupported struct type for: %s", fieldValue.Type())
		}
	default:
		return nil, fmt.Errorf("unsupported field type for: %s", fieldValue.Kind())
	}

	return value, nil
}

func (p *ReflectParserUtils) GetObjectFieldNames(obj interface{}) ([]string, error) {
	val := reflect.ValueOf(obj)

	// Dereference the pointer if necessary
	if val.Kind() == reflect.Ptr {
		val = val.Elem()
	}

	// Ensure the input is a struct
	if val.Kind() != reflect.Struct {
		return nil, fmt.Errorf("expected a struct but got %s", val.Kind())
	}

	typ := val.Type()
	fieldNames := make([]string, val.NumField())

	for i := 0; i < val.NumField(); i++ {
		fieldNames[i] = typ.Field(i).Name
	}

	return fieldNames, nil
}

var ReflectParser = ReflectParserUtils{}

func MapStruct(src interface{}, dest interface{}) error {
	srcValue := reflect.ValueOf(src)
	destValue := reflect.ValueOf(dest)

	// Ensure src and dest are pointers
	if srcValue.Kind() != reflect.Ptr || destValue.Kind() != reflect.Ptr {
		return errors.New("src and dest must be pointers to structs")
	}

	srcValue = srcValue.Elem()
	destValue = destValue.Elem()

	// Ensure both are structs
	if srcValue.Kind() != reflect.Struct || destValue.Kind() != reflect.Struct {
		return errors.New("src and dest must be structs")
	}

	srcType := srcValue.Type()

	// Iterate over src fields
	for i := 0; i < srcValue.NumField(); i++ {
		field := srcValue.Field(i)
		fieldName := srcType.Field(i).Name

		// Set the field in dest if it exists and is settable
		destField := destValue.FieldByName(fieldName)
		if destField.IsValid() && destField.CanSet() && destField.Type() == field.Type() {
			destField.Set(field)
		}
	}

	return nil
}
