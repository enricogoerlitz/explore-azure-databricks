package models

import (
	"time"
)

var DISTRIBUTORS_MODEL_NAME = "distributors"

type DistributorModel struct {
	ID        int    `gorm:"primaryKey"`
	Name      string `gorm:"not null;unique"`
	CreatedAt time.Time
	UpdatedAt time.Time
}

func (DistributorModel) TableName() string {
	return DISTRIBUTORS_MODEL_NAME
}

type DistributorResponse struct {
	ID        int    `gorm:"primaryKey"`
	Name      string `gorm:"not null;unique"`
	CreatedAt time.Time
	UpdatedAt time.Time
}

func (DistributorResponse) TableName() string {
	return DISTRIBUTORS_MODEL_NAME
}

type DistributorPOST struct {
	Name      string `gorm:"not null;unique"`
	CreatedAt time.Time
	UpdatedAt time.Time
}

func (DistributorPOST) TableName() string {
	return DISTRIBUTORS_MODEL_NAME
}

type DistributorPATCH struct {
	Name      string `gorm:"not null;unique"`
	UpdatedAt time.Time
}

func (DistributorPATCH) TableName() string {
	return DISTRIBUTORS_MODEL_NAME
}
