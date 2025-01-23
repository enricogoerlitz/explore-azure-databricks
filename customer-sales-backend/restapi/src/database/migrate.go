package database

import "customer-sales-backend/src/models"

func MigrateDBModels() {
	// DB.AutoMigrate(&Customer{}, &Product{}, &Order{})
	DB.AutoMigrate(
		&models.ProductCategoryModel{},
		&models.DistributorModel{},
		&models.ProductModel{},
		&models.UserModel{},
		&models.RegionModel{},
		&models.OrderModel{},
		&models.OrderItemModel{},
	)
}
