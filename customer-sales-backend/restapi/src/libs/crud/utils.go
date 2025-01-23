package crud

import (
	"customer-sales-backend/src/database"
	"customer-sales-backend/src/utils"
	"fmt"
	"reflect"
	"strconv"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func GetDBQuery(inputDBQuery *gorm.DB) *gorm.DB {
	if inputDBQuery == nil {
		return database.DB
	}

	return inputDBQuery
}

func PaginateDBQuery(c *gin.Context, dbQuery *gorm.DB, maxPageSize int) *gorm.DB {
	limit := maxPageSize
	offset := 0

	if c.Query("limit") != "" {
		if l, err := strconv.Atoi(c.Query("limit")); err == nil && l > 0 {
			limit = l
		}
	}

	if c.Query("offset") != "" {
		if o, err := strconv.Atoi(c.Query("offset")); err == nil && o >= 0 {
			offset = o
		}
	}

	return dbQuery.Limit(limit).Offset(offset)
}

func CheckForeignKeysExisting(
	payload reflect.Value,
	foreignKeyColumns []ForeignKeyColumn,
	checkAsRequired bool,
) error {
	if len(foreignKeyColumns) == 0 {
		return nil
	}

	for _, foreignKeyColumn := range foreignKeyColumns {
		if !checkAsRequired {
			fieldPrt := payload.FieldByName(foreignKeyColumn.Field)
			if (fieldPrt.Kind() == reflect.Int && fieldPrt.Int() == 0) ||
				(fieldPrt.Kind() == reflect.String && fieldPrt.String() == "") {
				continue
			}
		}

		model := &foreignKeyColumn.Model
		id, err := utils.ReflectParser.GetFieldValue(payload, foreignKeyColumn.Field)
		if err != nil {
			return err
		}

		var count int64
		if database.DB.Find(model, id).Count(&count); count == 0 {
			return fmt.Errorf("field '%s' not found with id=%d", foreignKeyColumn.Field, id)
		}
	}

	return nil
}

func CheckUniqueColumns[T any](payload reflect.Value, uniqueColumns []string) error {
	if len(uniqueColumns) == 0 {
		return nil
	}

	for _, column := range uniqueColumns {
		dbColumn := database.DB.NamingStrategy.ColumnName("", column)
		columnValue, err := utils.ReflectParser.GetFieldValue(payload, column)
		if err != nil {
			return err
		}

		var obj T
		var count int64
		if database.DB.Where(fmt.Sprintf("%s = ?", dbColumn), columnValue).Find(&obj).Count(&count); count > 0 {
			return fmt.Errorf("field %s must be unique", dbColumn)
		}
	}

	return nil
}

func CheckUniqueColumnsTogether[T any](payload reflect.Value, uniqueColumnsTogether [][]string) error {
	if len(uniqueColumnsTogether) == 0 {
		return nil
	}

	for _, uniqueColumnsTogetherPair := range uniqueColumnsTogether {
		dbQuery := database.DB

		for _, column := range uniqueColumnsTogetherPair {
			dbColumn := database.DB.NamingStrategy.ColumnName("", column)
			columnValue, err := utils.ReflectParser.GetFieldValue(payload, column)
			if err != nil {
				return err
			}
			dbQuery = dbQuery.Where(fmt.Sprintf("%s = ?", dbColumn), columnValue)
		}

		var obj T
		var count int64
		if dbQuery.Find(&obj).Count(&count); count > 0 {
			return fmt.Errorf("fields %v must be unique together", uniqueColumnsTogetherPair)
		}

	}

	return nil
}

func CheckUniquePrimaryKey(payload reflect.Value) error {
	// TODO: Implement
	return nil
}
