package models

import "time"

var USERS_MODEL_NAME = "users"

type UserModel struct {
	ID        int    `gorm:"primaryKey"`
	Firstname string `gorm:"not null"`
	Lastname  string `gorm:"not null"`
	Password  string `gorm:"not null"`
	CreatedAt time.Time
	UpdatedAt time.Time
}

func (UserModel) TableName() string {
	return USERS_MODEL_NAME
}

type UserResponse struct {
	ID        int    `gorm:"primaryKey"`
	Firstname string `gorm:"not null"`
	Lastname  string `gorm:"not null"`
	Password  string `gorm:"not null"`
	CreatedAt time.Time
	UpdatedAt time.Time
}

func (UserResponse) TableName() string {
	return USERS_MODEL_NAME
}

type UserPOST struct {
	Firstname string `gorm:"not null"`
	Lastname  string `gorm:"not null"`
	Password  string `gorm:"not null"`
}

func (UserPOST) TableName() string {
	return USERS_MODEL_NAME
}

type UserPATCH struct {
	Firstname string `gorm:"not null"`
	Lastname  string `gorm:"not null"`
}

func (UserPATCH) TableName() string {
	return USERS_MODEL_NAME
}
