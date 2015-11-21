# python-freezing-example

* Install with `python setup.py install`

* ```sh
  $ foo
  Foo was called!
  $ bar
  Bar was called!
  ```
## Things to remember
* `pyinstaller` can freeze one python script into a stand alone binary executable which can be executed by adding `./` prefix.
* Add the binary into one of your `$PATH` locations and the prefix is not required. That works as a program !
* `setuptools` provides the `entry_points` option for freezing a complete library. That's cool !

