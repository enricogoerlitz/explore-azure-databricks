package database

import (
	"context"
	"os"

	"github.com/Azure/azure-sdk-for-go/sdk/azidentity"
	"github.com/Azure/azure-sdk-for-go/sdk/keyvault/azsecrets"
	"github.com/sirupsen/logrus"

	"gorm.io/driver/sqlserver"
	"gorm.io/gorm"
)

var DB *gorm.DB // repository

func ConnectDB() {
	// os.Setenv("DB_HOST", "localhost")
	// os.Setenv("DB_USER", "sa")
	// os.Setenv("DB_PASSWORD", "adminpw1!")
	// os.Setenv("DB_NAME", "database")

	username, password, credsErr := getDatabaseCredentials()

	if credsErr != nil {
		logrus.Error("Failed to retrieve database credentisals.", credsErr.Error())
		panic("Failed to initialize gorm with the database connection")
	}

	// If the connection raises an error, maybe the database customersales is not created yet.
	connectionString :=
		"server=" + os.Getenv("DB_HOST") +
			";user id=" + username +
			";password=" + password +
			";database=" + os.Getenv("DB_NAME")

	var err error
	DB, err = gorm.Open(sqlserver.Open(connectionString), &gorm.Config{})

	if err != nil {
		logrus.Error("Failed to connect to the database because: ", err.Error())
		panic("Failed to initialize gorm with the database connection")
	} else {
		logrus.Info("Successfully connected to the database")
	}
}

func getDatabaseCredentials() (string, string, error) {
	if os.Getenv("MODE") == "release" {
		logrus.Info("Getting database credentials from Azure Key Vault")
		username, err := getKeyVaultSecret(os.Getenv("DB_USER_KV_SECRET_NAME"))
		if err != nil {
			return "", "", err
		}

		password, err := getKeyVaultSecret(os.Getenv("DB_PASSWORD_KV_SECRET_NAME"))
		if err != nil {
			return "", "", err
		}

		return username, password, err
	}

	logrus.Info("Getting database credentials from environment variables")
	return os.Getenv("DB_USER"), os.Getenv("DB_PASSWORD"), nil
}

func getKeyVaultSecret(secretName string) (string, error) {
	vaultUrl := os.Getenv("KEYVAULT_URL")
	cred, err := azidentity.NewDefaultAzureCredential(nil)
	if err != nil {
		return "", err
	}

	client, err := azsecrets.NewClient(vaultUrl, cred, nil)
	if err != nil {
		return "", err
	}

	resp, err := client.GetSecret(context.Background(), secretName, "", nil)
	if err != nil {
		return "", err
	}

	return *resp.Value, nil
}
