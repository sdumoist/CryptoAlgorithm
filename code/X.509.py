from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


# 生成X.509证书
def generate_x509_certificate(private_key, subject_name):
    builder = x509.CertificateBuilder()
    builder = builder.subject_name(subject_name)
    builder = builder.issuer_name(subject_name)
    builder = builder.not_valid_before(datetime.datetime.utcnow())
    builder = builder.not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
    builder = builder.serial_number(x509.random_serial_number())
    builder = builder.public_key(private_key.public_key())
    certificate = builder.sign(private_key, hashes.SHA256(), default_backend())
    return certificate


# 解析X.509证书
def parse_x509_certificate(certificate_pem):
    certificate = x509.load_pem_x509_certificate(certificate_pem, default_backend())
    return certificate


# 示例用法
# 生成RSA密钥对
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# 主题名称
subject_name = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Example Org"),
    x509.NameAttribute(NameOID.COMMON_NAME, "www.example.com"),
])

# 生成X.509证书
certificate = generate_x509_certificate(private_key, subject_name)

# 将证书转换为PEM格式
certificate_pem = certificate.public_bytes(encoding=serialization.Encoding.PEM)

# 解析X.509证书
parsed_certificate = parse_x509_certificate(certificate_pem)

# 打印解析后的证书信息
print("Subject:", parsed_certificate.subject)
print("Issuer:", parsed_certificate.issuer)
print("Serial Number:", parsed_certificate.serial_number)
print("Public Key:", parsed_certificate.public_key())
print("Not Before:", parsed_certificate.not_valid_before)
print("Not After:", parsed_certificate.not_valid_after)