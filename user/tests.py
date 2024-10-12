from django.test import TestCase
from django.contrib.auth import get_user_model

class UserAccountTests(TestCase):
    
    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'vicky@gmail.com', 'maurya.8' ,'123456',
        )
        self.assertEqual( super_user.email , 'vicky@gmail.com')
        self.assertEqual( super_user.user_name,'maurya.8')
        self.assertTrue( super_user.is_superuser)
        self.assertTrue( super_user.is_staff)
        self.assertTrue( super_user.is_active)
        self.assertEqual(str(super_user),'maurya.8')
        
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='vicky@gmail.com',
                user_name ='maurya.8',
                password = '123456',
                is_superuser = False,
            )
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='vicky@gmail.com',
                user_name ='maurya.8',
                password = '123456',
                is_staff = False,
            )    
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='',
                user_name ='maurya.8',
                password = '123456',
                is_superuser = False,
            )    
    
    def test_new_user(self):
        
        db = get_user_model()
        user = db.objects.create_user(
            'vicky1@gmail.com', 'maurya.18' ,'123456'
        )
        self.assertEqual( user.email , 'vicky1@gmail.com')
        self.assertEqual( user.user_name,'maurya.18')
        self.assertFalse( user.is_superuser)
        self.assertFalse( user.is_staff)
        self.assertFalse( user.is_active)
        self.assertEqual(str(user),'maurya.18')
        
        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='',
                user_name ='maurya.18',
                password = '123456',
                is_superuser = False
            )   
            