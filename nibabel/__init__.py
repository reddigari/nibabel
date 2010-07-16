# emacs: -*- mode: python-mode; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the NiBabel package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""This package provides read and write access to some common
neuroimaging file formats.

The various image format classes give full or selective access to header
(meta) information and access to the image data is made available via
NumPy arrays.

============
 Quickstart
============

::

   import nibabel as nib

   img1 = nib.load('my_file.nii')
   img2 = nib.load('other_file.nii.gz')
   img3 = nib.load('spm_file.img')

   data = img1.get_data()
   affine = img1.get_affine()

   print img1

   nib.save(img1, 'my_file_copy.nii.gz')

   new_image = nib.Nifti1Image(data, affine)
   nib.save(new_image, 'new_image.nii.gz')

"""

__docformat__ = 'restructuredtext'

# canonical version string
__version__ = '1.0.0'


# module imports
from nibabel import analyze as ana
from nibabel import spm99analyze as spm99
from nibabel import spm2analyze as spm2
from nibabel import nifti1 as ni1
from nibabel import minc
# object imports
from nibabel.fileholders import FileHolder, FileHolderError
from nibabel.loadsave import load, save
from nibabel.analyze import AnalyzeHeader, AnalyzeImage
from nibabel.spm99analyze import Spm99AnalyzeHeader, Spm99AnalyzeImage
from nibabel.spm2analyze import Spm2AnalyzeHeader, Spm2AnalyzeImage
from nibabel.nifti1 import Nifti1Header, Nifti1Image, Nifti1Pair
from nibabel.minc import MincImage
from nibabel.funcs import (squeeze_image, concat_images, four_to_three,
                           as_closest_canonical)
from nibabel.orientations import (io_orientation, orientation_affine,
                                  flip_axis, OrientationError,
                                  apply_orientation)
from nibabel.imageclasses import class_map, ext_map