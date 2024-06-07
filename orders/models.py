from django.db import models

# Create your models here.
class Customers(models.Model):
    customernumber = models.IntegerField(db_column='customerNumber', primary_key=True,verbose_name="客戶編號")  # Field name made lowercase.
    customername = models.CharField(db_column='customerName', max_length=50,verbose_name="客戶名稱")  # Field name made lowercase.
    contactlastname = models.CharField(db_column='contactLastName', max_length=50,verbose_name="聯絡人姓氏")  # Field name made lowercase.
    contactfirstname = models.CharField(db_column='contactFirstName', max_length=50,verbose_name="聯絡人名字")  # Field name made lowercase.
    phone = models.CharField(max_length=50,verbose_name="電話")
    addressline1 = models.CharField(db_column='addressLine1', max_length=50,verbose_name="地址1")  # Field name made lowercase.
    addressline2 = models.CharField(db_column='addressLine2', max_length=50, blank=True, null=True,verbose_name="地址2")  # Field name made lowercase.
    city = models.CharField(max_length=50,verbose_name="城市")
    state = models.CharField(max_length=50, blank=True, null=True,verbose_name="州")
    postalcode = models.CharField(db_column='postalCode', max_length=15, blank=True, null=True,verbose_name="郵遞區號")  # Field name made lowercase.
    country = models.CharField(max_length=50,verbose_name="國家")
    salesrepemployeenumber = models.ForeignKey('Employees', models.DO_NOTHING, db_column='salesRepEmployeeNumber', blank=True, null=True,verbose_name="銷售代表員工編號")  # Field name made lowercase.
    creditlimit = models.DecimalField(db_column='creditLimit', max_digits=10, decimal_places=2, blank=True, null=True,verbose_name="信用額度")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'

    def __str__(self) -> str:
        return f"{self.customernumber} - {self.customername}"


class Employees(models.Model):
    employeenumber = models.IntegerField(db_column='employeeNumber', primary_key=True,verbose_name="員工編號")  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50,verbose_name="姓氏")  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=50,verbose_name="名字")  # Field name made lowercase.
    extension = models.CharField(max_length=10,verbose_name="分機")
    email = models.CharField(max_length=100,verbose_name="電子郵件")
    officecode = models.ForeignKey('Offices', models.DO_NOTHING, db_column='officeCode',verbose_name="辦公室代碼")  # Field name made lowercase.
    reportsto = models.ForeignKey('self', models.DO_NOTHING, db_column='reportsTo', blank=True, null=True,verbose_name="匯報對象")  # Field name made lowercase.
    jobtitle = models.CharField(db_column='jobTitle', max_length=50,verbose_name="職稱")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employees'


class Offices(models.Model):
    officecode = models.CharField(db_column='officeCode', primary_key=True, max_length=10,verbose_name="辦公室代碼")  # Field name made lowercase.
    city = models.CharField(max_length=50,verbose_name="城市")
    phone = models.CharField(max_length=50,verbose_name="電話")
    addressline1 = models.CharField(db_column='addressLine1', max_length=50,verbose_name="地址1")  # Field name made lowercase.
    addressline2 = models.CharField(db_column='addressLine2', max_length=50, blank=True, null=True,verbose_name="地址2")  # Field name made lowercase.
    state = models.CharField(max_length=50, blank=True, null=True,verbose_name="州")
    country = models.CharField(max_length=50,verbose_name="國家")
    postalcode = models.CharField(db_column='postalCode', max_length=15,verbose_name="郵遞區號")  # Field name made lowercase.
    territory = models.CharField(max_length=10,verbose_name="區域")

    class Meta:
        managed = False
        db_table = 'offices'

# 複合主鍵
class OrderdetailsManager(models.Manager):
    def get_by_natural_key(self, ordernumber, productcode):
        return self.get(ordernumber=ordernumber, productcode=productcode)


class Orderdetails(models.Model):
    ordernumber = models.ForeignKey('Orders', models.DO_NOTHING, db_column='orderNumber', primary_key=True,verbose_name="訂單編號")  # Field name made lowercase. The composite primary key (orderNumber, productCode) found, that is not supported. The first column is selected.
    productcode = models.ForeignKey('Products', models.DO_NOTHING, db_column='productCode',verbose_name="產品代碼")  # Field name made lowercase.
    quantityordered = models.IntegerField(db_column='quantityOrdered',verbose_name="訂購數量")  # Field name made lowercase.
    priceeach = models.DecimalField(db_column='priceEach', max_digits=10, decimal_places=2,verbose_name="單價")  # Field name made lowercase.
    orderlinenumber = models.SmallIntegerField(db_column='orderLineNumber',verbose_name="訂單行號")  # Field name made lowercase.

    objects = OrderdetailsManager()
    class Meta:
        managed = False
        db_table = 'orderdetails'
        unique_together = (('ordernumber', 'productcode'),)

    def natural_key(self):
        return (self.ordernumber, self.productcode)
    
    def save(self, *args, **kwargs):
        if not self.id:
            # Perform a custom check or action here if needed
            pass
        super(Orderdetails, self).save(*args, **kwargs)



class Orders(models.Model):
    ordernumber = models.IntegerField(db_column='orderNumber', primary_key=True,verbose_name="訂單編號")  # Field name made lowercase.
    orderdate = models.DateField(db_column='orderDate',verbose_name="訂單日期")  # Field name made lowercase.
    requireddate = models.DateField(db_column='requiredDate',verbose_name="要求日期")  # Field name made lowercase.
    shippeddate = models.DateField(db_column='shippedDate', blank=True, null=True,verbose_name="發貨日期")  # Field name made lowercase.
    status = models.CharField(max_length=15,verbose_name="狀態")
    comments = models.TextField(blank=True, null=True,verbose_name="評論")
    customernumber = models.ForeignKey(Customers, models.DO_NOTHING, db_column='customerNumber',verbose_name="客戶編號")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'

    # def __str__(self) -> str:
    #     return f"{self.ordernumber} - {self.comments}"


class Payments(models.Model):
    customernumber = models.OneToOneField(Customers, models.DO_NOTHING, db_column='customerNumber', primary_key=True,verbose_name="客戶編號")  # Field name made lowercase. The composite primary key (customerNumber, checkNumber) found, that is not supported. The first column is selected.
    checknumber = models.CharField(db_column='checkNumber', max_length=50,verbose_name="支票號碼")  # Field name made lowercase.
    paymentdate = models.DateField(db_column='paymentDate',verbose_name="付款日期")  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="金額")

    class Meta:
        managed = False
        db_table = 'payments'
        unique_together = (('customernumber', 'checknumber'),)


class Productlines(models.Model):
    productline = models.CharField(db_column='productLine', primary_key=True, max_length=50,verbose_name="產品線")  # Field name made lowercase.
    textdescription = models.CharField(db_column='textDescription', max_length=4000, blank=True, null=True,verbose_name="描述")  # Field name made lowercase.
    htmldescription = models.TextField(db_column='htmlDescription', blank=True, null=True,verbose_name="其他描述")  # Field name made lowercase.
    image = models.TextField(blank=True, null=True,verbose_name="圖片")

    class Meta:
        managed = False
        db_table = 'productlines'


class Products(models.Model):
    productcode = models.CharField(db_column='productCode', primary_key=True, max_length=1,verbose_name=" 產品代碼")  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=70,verbose_name="產品名稱")  # Field name made lowercase.
    productline = models.ForeignKey(Productlines, models.DO_NOTHING, db_column='productLine',verbose_name="產品線")  # Field name made lowercase.
    productscale = models.CharField(db_column='productScale', max_length=10,verbose_name="產品比例")  # Field name made lowercase.
    productvendor = models.CharField(db_column='productVendor', max_length=50,verbose_name="產品供應商")  # Field name made lowercase.
    productdescription = models.TextField(db_column='productDescription',verbose_name="產品描述")  # Field name made lowercase.
    quantityinstock = models.SmallIntegerField(db_column='quantityInStock',verbose_name="庫存數量")  # Field name made lowercase.
    buyprice = models.DecimalField(db_column='buyPrice', max_digits=10, decimal_places=2,verbose_name="購買價格")  # Field name made lowercase.
    msrp = models.DecimalField(db_column='MSRP', max_digits=10, decimal_places=2,verbose_name="建議零售價")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'products'

    def __str__(self) -> str:
        return f"{self.productcode} - {self.productname}"
    
    


    #權限
    from django.db import models

class YourModel(models.Model):
    # 定義你的模型字段
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        permissions = [
            ("can_view_customers", "Can view customers"),
            ("can_view_employees", "Can view employees"),
            ("can_view_offices", "Can view offices"),
        ]