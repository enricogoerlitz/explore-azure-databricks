package models

import "time"

var ORDER_ITEMS_MODEL_NAME = "order_items"

type OrderItemModel struct {
	ID           int          `gorm:"primaryKey"`
	OrderID      int          `gorm:"not null"`
	Order        OrderModel   `gorm:"foreignKey:OrderID"`
	ProductID    int          `gorm:"not null"`
	Product      ProductModel `gorm:"foreignKey:ProductID"`
	ProductPrice float64      `gorm:"not null"`
	Quantity     int          `gorm:"not null"`
	Status       string       `gorm:"not null"`
	CreatedAt    time.Time
	UpdatedAt    time.Time
}

func (OrderItemModel) TableName() string {
	return ORDER_ITEMS_MODEL_NAME
}

type OrderItemResponse struct {
	ID           int     `gorm:"primaryKey"`
	OrderID      int     `gorm:"not null"`
	ProductID    int     `gorm:"not null"`
	ProductPrice float64 `gorm:"not null"`
	Quantity     int     `gorm:"not null"`
	Status       string  `gorm:"not null"`
	CreatedAt    time.Time
	UpdatedAt    time.Time
}

func (OrderItemResponse) TableName() string {
	return ORDER_ITEMS_MODEL_NAME
}

type OrderItemPOST struct {
	OrderID      int     `gorm:"not null"`
	ProductID    int     `gorm:"not null"`
	ProductPrice float64 `gorm:"not null"`
	Quantity     int     `gorm:"not null"`
	Status       string  `gorm:"not null"`
	CreatedAt    time.Time
	UpdatedAt    time.Time
}

func (OrderItemPOST) TableName() string {
	return ORDER_ITEMS_MODEL_NAME
}

type OrderItemPATCH struct {
	OrderID      int     `gorm:"not null"`
	ProductID    int     `gorm:"not null"`
	ProductPrice float64 `gorm:"not null"`
	Quantity     int     `gorm:"not null"`
	Status       string  `gorm:"not null"`
	UpdatedAt    time.Time
}

func (OrderItemPATCH) TableName() string {
	return ORDER_ITEMS_MODEL_NAME
}
