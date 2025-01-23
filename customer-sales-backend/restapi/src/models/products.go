package models

import "time"

var PRODUCTS_MODEL_NAME = "products"

type ProductModel struct {
	ID            int    `gorm:"primaryKey"`
	Name          string `gorm:"not null;unique"`
	Description   string
	Price         float64              `gorm:"not null"`
	CategoryID    int                  `gorm:"not null"`
	Category      ProductCategoryModel `gorm:"foreignKey:CategoryID"`
	DistributorID int                  `gorm:"not null"`
	Distributor   DistributorModel     `gorm:"foreignKey:DistributorID"`
	CreatedAt     time.Time
	UpdatedAt     time.Time
}

func (ProductModel) TableName() string {
	return PRODUCTS_MODEL_NAME
}

type ProductResponse struct {
	ID            int    `gorm:"primaryKey"`
	Name          string `gorm:"not null;unique"`
	Description   string
	Price         float64 `gorm:"not null"`
	CategoryID    int     `gorm:"not null"`
	DistributorID int     `gorm:"not null"`
	CreatedAt     time.Time
	UpdatedAt     time.Time
}

func (ProductResponse) TableName() string {
	return PRODUCTS_MODEL_NAME
}

type ProductPOST struct {
	Name          string `gorm:"not null;unique"`
	Description   string
	Price         float64 `gorm:"not null"`
	CategoryID    int     `gorm:"not null"`
	DistributorID int     `gorm:"not null"`
	CreatedAt     time.Time
	UpdatedAt     time.Time
}

func (ProductPOST) TableName() string {
	return PRODUCTS_MODEL_NAME
}

type ProductPATCH struct {
	Name          string `gorm:"not null;unique"`
	Description   string
	Price         float64 `gorm:"not null"`
	CategoryID    int     `gorm:"not null"`
	DistributorID int     `gorm:"not null"`
	UpdatedAt     time.Time
}

func (ProductPATCH) TableName() string {
	return PRODUCTS_MODEL_NAME
}
