from distutils.core import setup
import setup_translate


setup(name='enigma2-plugin-systemplugins-xmlupdate',
		version='1.0',
		author='Huevos/ahmedmoselhi',
		author_email='ahmedmoselhi55@gmail.com',
		package_dir={'SystemPlugins.XmlUpdate': 'src'},
		packages=['SystemPlugins.XmlUpdate'],
		package_data={'SystemPlugins.XmlUpdate': ['']},
		description='Fetches and updates transponder xml files',
		cmdclass=setup_translate.cmdclass)
