package utils

type StringArrayUtils struct{}
type ArrayUtils struct {
	String StringArrayUtils
}

func (a *StringArrayUtils) Contains(slice []string, str string) bool {
	for _, v := range slice {
		if v == str {
			return true
		}
	}
	return false
}

var Array = ArrayUtils{}
