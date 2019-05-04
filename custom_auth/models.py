from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin)

LOCATIONS = (
    ('10', '서울'),
    ('20', '강원'),
    ('30', '대전'),
    ('31', '충남'),
    ('33', '세종'),
    ('36', '충북'),
    ('40', '인천'),
    ('41', '경기'),
    ('50', '광주'),
    ('51', '전남'),
    ('56', '전북'),
    ('60', '부산'),
    ('62', '경남'),
    ('68', '울산'),
    ('69', '제주'),
    ('70', '대구'),
    ('71', '경북'),
)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=CustomUserManager.normalize_email(email),
            username=username,
        )

        user.is_active = True
        user.is_staff = False
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        u = self.create_user(email=email,
                             username=username,
                             password=password)
        u.is_staff = True
        u.is_active = True
        u.save(using=self._db)
        return u


class CustomUser(AbstractBaseUser,  PermissionsMixin):
    """
    # CustomUser Model
    회원이 가지는 정보들을 저장한다.
    
    ## 가입에 필요한 정보
    * email        : 가입신청할때 쓰는 이메일
    * real_name    : 회원의 이름
    * age          : 회원의 나이
    * phone_number : 회원의 전화번호를 나타낸다.

    * address1      : 회원이 거주하는 장소를 나타낸다.
    
    ## 커뮤니티를 이용할 때 필요한 정보
    * is_active  : 시스템에 접근할 권한이 있는지 여부를 나타낸다.
    * is_staff   : 운영자인지를 나타낸다.
    * username   : 서비스에서 사용할 ID
    """
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )

    real_name = models.CharField(
        verbose_name='real_name',
        max_length=20,
        default="홍길동",
        blank=False
    )

    phone_number = models.CharField(
        verbose_name='phone_number',
        default="010-0000-0000",
        max_length=20,
        blank=False
    )    

    age = models.IntegerField(
        verbose_name='age',
        default=0,
        blank=False
    )
    
    address1 = models.CharField(
        verbose_name='address1',
        max_length=2,
        choices=LOCATIONS,
        default='10',
        blank=False
    )

    is_paid = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    username = models.CharField(
        verbose_name='username',
        max_length=20,
        blank=False,
        unique=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        app_label = 'custom_auth'
        db_table = "custom_user"
        default_permissions = ()

        """
        Database에서의 검색속도 향상을 위해 인덱스를 적용할 칼럼
        * email로 검색해도 빠르게 검색이 가능해야 한다.
        * username로 검색해도 빠르게 검색이 가능해야 한다.
        """
        indexes = [
            models.Index(fields=['email',]),
            models.Index(fields=['username',]),
        ]

    def get_full_name(self):
        # The user is identified by their username
        return self.username

    def get_short_name(self):
        # The user is identified by their username
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_admin(self):
        return self.is_staff