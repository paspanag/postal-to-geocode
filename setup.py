from setuptools import setup


def _post_install(setup):
    from postal_to_geocode import setup_db
    print('setting up db file')
    setup_db()
    return setup


_post_install(
    setup(
        name='Postal To Geocode',
        version='0.01b',
        packages=['postal_to_geocode',],
        license='Creative Commons Attribution-Noncommercial-Share Alike license',
        long_description=open('README.txt').read(),
        include_package_data=True,
        install_requires=[
            'requests==2.25.1',
        ],
        zip_safe=False,
    ))
