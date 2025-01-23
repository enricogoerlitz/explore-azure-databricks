package models

import "time"

var REGIONS_MODEL_NAME = "regions"

type RegionModel struct {
	ID        int    `gorm:"primaryKey"`
	Name      string `gorm:"not null;unique"`
	Long      float64
	Lat       float64
	CreatedAt time.Time
	UpdatedAt time.Time
}

func (RegionModel) TableName() string {
	return REGIONS_MODEL_NAME
}

type RegionResponse struct {
	ID        int    `gorm:"primaryKey"`
	Name      string `gorm:"not null;unique"`
	Long      float64
	Lat       float64
	CreatedAt time.Time
	UpdatedAt time.Time
}

func (RegionResponse) TableName() string {
	return REGIONS_MODEL_NAME
}

type RegionPOST struct {
	Name      string `gorm:"not null;unique"`
	Long      float64
	Lat       float64
	CreatedAt time.Time
	UpdatedAt time.Time
}

func (RegionPOST) TableName() string {
	return REGIONS_MODEL_NAME
}

type RegionPATCH struct {
	Name      string `gorm:"not null;unique"`
	Long      float64
	Lat       float64
	UpdatedAt time.Time
}

func (RegionPATCH) TableName() string {
	return REGIONS_MODEL_NAME
}
