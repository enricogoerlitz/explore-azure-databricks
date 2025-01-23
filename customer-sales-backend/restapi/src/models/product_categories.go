package models

import "time"

var PRODUCT_CATEGORIES_MODEL_NAME = "product_categories"

type ProductCategoryModel struct {
	ID          int    `gorm:"primaryKey"`
	Name        string `gorm:"not null;unique"`
	Description string
	CreatedAt   time.Time
	UpdatedAt   time.Time
}

func (ProductCategoryModel) TableName() string {
	return PRODUCT_CATEGORIES_MODEL_NAME
}

type ProductCategoryResponse struct {
	ID          int    `gorm:"primaryKey"`
	Name        string `gorm:"not null;unique"`
	Description string
	CreatedAt   time.Time
	UpdatedAt   time.Time
}

func (ProductCategoryResponse) TableName() string {
	return PRODUCT_CATEGORIES_MODEL_NAME
}

type ProductCategoryPOST struct {
	Name        string `gorm:"not null;unique"`
	Description string
	CreatedAt   time.Time
	UpdatedAt   time.Time
}

func (ProductCategoryPOST) TableName() string {
	return PRODUCT_CATEGORIES_MODEL_NAME
}

type ProductCategoryPATCH struct {
	Name        string `gorm:"not null;unique"`
	Description string
	UpdatedAt   time.Time
}

func (ProductCategoryPATCH) TableName() string {
	return PRODUCT_CATEGORIES_MODEL_NAME
}
