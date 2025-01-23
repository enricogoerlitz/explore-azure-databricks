package models

import "time"

var ORDERS_MODEL_NAME = "orders"

type OrderModel struct {
	ID                  int         `gorm:"primaryKey"`
	UserID              int         `gorm:"not null"`
	User                UserModel   `gorm:"foreignKey:UserID;references:ID"`
	DestinationRegionID int         `gorm:"not null"`
	Region              RegionModel `gorm:"foreignKey:DestinationRegionID;references:ID"`
	TotalPrice          float64     `gorm:"not null"`
	Status              string      `gorm:"not null"`
	OrderDate           time.Time
	CreatedAt           time.Time
	UpdatedAt           time.Time
}

func (OrderModel) TableName() string {
	return ORDERS_MODEL_NAME
}

type OrderResponse struct {
	ID                  int     `gorm:"primaryKey"`
	UserID              int     `gorm:"not null"`
	DestinationRegionID int     `gorm:"not null"`
	TotalPrice          float64 `gorm:"not null"`
	Status              string  `gorm:"not null"`
	OrderDate           time.Time
	CreatedAt           time.Time
	UpdatedAt           time.Time
}

func (OrderResponse) TableName() string {
	return ORDERS_MODEL_NAME
}

type OrderResponseDetail struct {
	ID                  int         `gorm:"primaryKey"`
	UserID              int         `gorm:"not null"`
	User                UserModel   `gorm:"foreignKey:UserID"`
	DestinationRegionID int         `gorm:"not null"`
	Region              RegionModel `gorm:"foreignKey:DestinationRegionID"`
	TotalPrice          float64     `gorm:"not null"`
	Status              string      `gorm:"not null"`
	OrderDate           time.Time
	CreatedAt           time.Time
	UpdatedAt           time.Time
	OrderItems          []OrderItemResponse `gorm:"foreignKey:OrderID;references:ID"`
}

func (OrderResponseDetail) TableName() string {
	return ORDERS_MODEL_NAME
}

type OrderPayloadPOST struct {
	UserID              int     `gorm:"not null"`
	DestinationRegionID int     `gorm:"not null"`
	TotalPrice          float64 `gorm:"not null"`
	Status              string  `gorm:"not null"`
	OrderDate           time.Time
	CreatedAt           time.Time
	UpdatedAt           time.Time
}

func (OrderPayloadPOST) TableName() string {
	return ORDERS_MODEL_NAME
}

type OrderPayloadPATCH struct {
	UserID              int     `gorm:"not null"`
	DestinationRegionID int     `gorm:"not null"`
	TotalPrice          float64 `gorm:"not null"`
	OrderDate           time.Time
	UpdatedAt           time.Time
}

func (OrderPayloadPATCH) TableName() string {
	return ORDERS_MODEL_NAME
}
