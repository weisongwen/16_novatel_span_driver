# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from novatel_msgs/BESTPOS.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import novatel_msgs.msg

class BESTPOS(genpy.Message):
  _md5sum = "8321b9523105411643891c8653878967"
  _type = "novatel_msgs/BESTPOS"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# message 42
novatel_msgs/CommonHeader header

# Table 21 in the SPAN on OEM6 manual.
# See: http://www.novatel.com/assets/Documents/Manuals/OM-20000144UM.pdf#page=99
uint32 solution_status
uint32 SOLUTION_STATUS_SOLUTION_COMPUTED=0
uint32 SOLUTION_STATUS_INSUFFICIENT_OBSERVATIONS=1
uint32 SOLUTION_STATUS_NO_CONVERGENCE=2
uint32 SOLUTION_STATUS_SINGULARITY_AT_PARAMETERS_MATRIX=3
uint32 SOLUTION_STATUS_COVARIANCE_TRACE_EXCEEDS_MAXIMUM=4
uint32 SOLUTION_STATUS_TEST_DISTANCE_EXCEEDED=5
uint32 SOLUTION_STATUS_COLD_START=6
uint32 SOLUTION_STATUS_VELOCITY_OR_HEIGHT_LIMIT_EXCEEDED=7
uint32 SOLUTION_STATUS_VARIANCE_EXCEEDS_LIMITS=8
uint32 SOLUTION_STATUS_RESIDUALS_TOO_LARGE=9
uint32 SOLUTION_STATUS_INTEGRITY_WARNING=13
uint32 SOLUTION_STATUS_PENDING=18
uint32 SOLUTION_STATUS_INVALID_FIX=19
uint32 SOLUTION_STATUS_INVALID_RATE=22

# Table 22 in the SPAN on OEM6 manual.
# http://www.novatel.com/assets/Documents/Manuals/OM-20000144UM.pdf#page=100
uint32 position_type
uint32 POSITION_TYPE_NONE=0
uint32 POSITION_TYPE_FIXED=1
uint32 POSITION_TYPE_FIXEDHEIGHT=2
uint32 POSITION_TYPE_FLOATCONV=4
uint32 POSITION_TYPE_WIDELANE=5
uint32 POSITION_TYPE_NARROWLANE=6
uint32 POSITION_TYPE_DOPPLER_VELOCITY=8
uint32 POSITION_TYPE_SINGLE=16
uint32 POSITION_TYPE_PSRDIFF=17
uint32 POSITION_TYPE_WAAS=18
uint32 POSITION_TYPE_PROPAGATED=19
uint32 POSITION_TYPE_OMNISTAR=20
uint32 POSITION_TYPE_L1_FLOAT=32
uint32 POSITION_TYPE_IONOFREE_FLOAT=33
uint32 POSITION_TYPE_NARROW_FLOAT=34
uint32 POSITION_TYPE_L1_INT=48
uint32 POSITION_TYPE_WIDE_INT=49
uint32 POSITION_TYPE_NARROW_INT=50
uint32 POSITION_TYPE_RTK_DIRECT_INS=51
uint32 POSITION_TYPE_INS_SBAS=52
uint32 POSITION_TYPE_INS_PSRSP=53
uint32 POSITION_TYPE_INS_PSRDIFF=54
uint32 POSITION_TYPE_INS_RTKFLOAT=55
uint32 POSITION_TYPE_INS_RTKFIXED=56
uint32 POSITION_TYPE_INS_OMNISTAR=57
uint32 POSITION_TYPE_INS_OMNISTAR_HP=58
uint32 POSITION_TYPE_INS_OMNISTAR_XP=59
uint32 POSITION_TYPE_OMNISTAR_HP=64
uint32 POSITION_TYPE_OMNISTAR_XP=65
uint32 POSITION_TYPE_PPP_CONVERGING=68
uint32 POSITION_TYPE_PPP=69
uint32 POSITION_TYPE_INS_PPP_CONVERGING=73
uint32 POSITION_TYPE_INS_PPP=74

float64 latitude
float64 longitude
float64 altitude

float32 undulation
uint32 datum_id

float32 latitude_std
float32 longitude_std
float32 altitude_std

char[4] stn_id

float32 diff_age
float32 sol_age

uint8 svs
uint8 sol_svs
uint8 l1_svs
uint8 mult_svs
uint8 reserved
uint8 extsolstat
uint8 gal_sig_mask
uint8 sig_mask


================================================================================
MSG: novatel_msgs/CommonHeader
# On the wire, this header is preceeded by three sync bytes,
# which are 0xAA 0x44 0x12, and a uint8 which is the header length.

# Message ID of the log being output.
uint16 id

# Measurement source, format, response bit.
uint8 msg_type

uint8 port_addr
uint16 length
uint16 sequence

uint8 idle_time
uint8 time_status

uint16 gps_week
uint32 gps_week_seconds

# Table 3 in the SPAN on OEM6 manual.
# See: http://www.novatel.com/assets/Documents/Manuals/OM-20000144UM.pdf#page=13
uint32 receiver_status
uint32 RECEIVER_STATUS_ERROR=1
uint32 RECEIVER_STATUS_TEMPERATURE_WARNING=2
uint32 RECEIVER_STATUS_VOLTAGE_SUPPLY_WARNING=4
uint32 RECEIVER_STATUS_ANTENNA_UNPOWERED=8
uint32 RECEIVER_STATUS_LNA_FAILURE=16
uint32 RECEIVER_STATUS_ANTENNA_OPEN=32
uint32 RECEIVER_STATUS_ANTENNA_SHORTED=64
uint32 RECEIVER_STATUS_CPU_OVERLOADED=128
uint32 RECEIVER_STATUS_COM1_BUFFER_OVERRUN=256
uint32 RECEIVER_STATUS_COM2_BUFFER_OVERRUN=512
uint32 RECEIVER_STATUS_COM3_BUFFER_OVERRUN=1024
uint32 RECEIVER_STATUS_LINK_OVERLOAD=2048
uint32 RECEIVER_STATUS_AUX_TRANSMIT_OVERRUN=8192
uint32 RECEIVER_STATUS_AGC_OUT_OF_RANGE=16384
uint32 RECEIVER_STATUS_INS_RESET=65536
uint32 RECEIVER_STATUS_ALMANAC_INVALID=262144
uint32 RECEIVER_STATUS_POSITION_SOLUTION_INVALID=524288
uint32 RECEIVER_STATUS_POSITION_NOT_FIXED=1048576
uint32 RECEIVER_STATUS_CLOCK_STEERING_DISABLED=2097152
uint32 RECEIVER_STATUS_CLOCK_MODEL_INVALID=4194304
uint32 RECEIVER_STATUS_EXTERNAL_OSCILLATOR_LOCKED=8388608
uint32 RECEIVER_STATUS_SOFTWARE_RESOURCE_WARNING=16777216
uint32 RECEIVER_STATUS_AUXILIARY3_EVENT=536870912
uint32 RECEIVER_STATUS_AUXILIARY2_EVENT=1073741824
uint32 RECEIVER_STATUS_AUXILIARY1_EVENT=2147483648

uint16 reserved
uint16 software_version

"""
  # Pseudo-constants
  SOLUTION_STATUS_SOLUTION_COMPUTED = 0
  SOLUTION_STATUS_INSUFFICIENT_OBSERVATIONS = 1
  SOLUTION_STATUS_NO_CONVERGENCE = 2
  SOLUTION_STATUS_SINGULARITY_AT_PARAMETERS_MATRIX = 3
  SOLUTION_STATUS_COVARIANCE_TRACE_EXCEEDS_MAXIMUM = 4
  SOLUTION_STATUS_TEST_DISTANCE_EXCEEDED = 5
  SOLUTION_STATUS_COLD_START = 6
  SOLUTION_STATUS_VELOCITY_OR_HEIGHT_LIMIT_EXCEEDED = 7
  SOLUTION_STATUS_VARIANCE_EXCEEDS_LIMITS = 8
  SOLUTION_STATUS_RESIDUALS_TOO_LARGE = 9
  SOLUTION_STATUS_INTEGRITY_WARNING = 13
  SOLUTION_STATUS_PENDING = 18
  SOLUTION_STATUS_INVALID_FIX = 19
  SOLUTION_STATUS_INVALID_RATE = 22
  POSITION_TYPE_NONE = 0
  POSITION_TYPE_FIXED = 1
  POSITION_TYPE_FIXEDHEIGHT = 2
  POSITION_TYPE_FLOATCONV = 4
  POSITION_TYPE_WIDELANE = 5
  POSITION_TYPE_NARROWLANE = 6
  POSITION_TYPE_DOPPLER_VELOCITY = 8
  POSITION_TYPE_SINGLE = 16
  POSITION_TYPE_PSRDIFF = 17
  POSITION_TYPE_WAAS = 18
  POSITION_TYPE_PROPAGATED = 19
  POSITION_TYPE_OMNISTAR = 20
  POSITION_TYPE_L1_FLOAT = 32
  POSITION_TYPE_IONOFREE_FLOAT = 33
  POSITION_TYPE_NARROW_FLOAT = 34
  POSITION_TYPE_L1_INT = 48
  POSITION_TYPE_WIDE_INT = 49
  POSITION_TYPE_NARROW_INT = 50
  POSITION_TYPE_RTK_DIRECT_INS = 51
  POSITION_TYPE_INS_SBAS = 52
  POSITION_TYPE_INS_PSRSP = 53
  POSITION_TYPE_INS_PSRDIFF = 54
  POSITION_TYPE_INS_RTKFLOAT = 55
  POSITION_TYPE_INS_RTKFIXED = 56
  POSITION_TYPE_INS_OMNISTAR = 57
  POSITION_TYPE_INS_OMNISTAR_HP = 58
  POSITION_TYPE_INS_OMNISTAR_XP = 59
  POSITION_TYPE_OMNISTAR_HP = 64
  POSITION_TYPE_OMNISTAR_XP = 65
  POSITION_TYPE_PPP_CONVERGING = 68
  POSITION_TYPE_PPP = 69
  POSITION_TYPE_INS_PPP_CONVERGING = 73
  POSITION_TYPE_INS_PPP = 74

  __slots__ = ['header','solution_status','position_type','latitude','longitude','altitude','undulation','datum_id','latitude_std','longitude_std','altitude_std','stn_id','diff_age','sol_age','svs','sol_svs','l1_svs','mult_svs','reserved','extsolstat','gal_sig_mask','sig_mask']
  _slot_types = ['novatel_msgs/CommonHeader','uint32','uint32','float64','float64','float64','float32','uint32','float32','float32','float32','char[4]','float32','float32','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,solution_status,position_type,latitude,longitude,altitude,undulation,datum_id,latitude_std,longitude_std,altitude_std,stn_id,diff_age,sol_age,svs,sol_svs,l1_svs,mult_svs,reserved,extsolstat,gal_sig_mask,sig_mask

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(BESTPOS, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = novatel_msgs.msg.CommonHeader()
      if self.solution_status is None:
        self.solution_status = 0
      if self.position_type is None:
        self.position_type = 0
      if self.latitude is None:
        self.latitude = 0.
      if self.longitude is None:
        self.longitude = 0.
      if self.altitude is None:
        self.altitude = 0.
      if self.undulation is None:
        self.undulation = 0.
      if self.datum_id is None:
        self.datum_id = 0
      if self.latitude_std is None:
        self.latitude_std = 0.
      if self.longitude_std is None:
        self.longitude_std = 0.
      if self.altitude_std is None:
        self.altitude_std = 0.
      if self.stn_id is None:
        self.stn_id = chr(0)*4
      if self.diff_age is None:
        self.diff_age = 0.
      if self.sol_age is None:
        self.sol_age = 0.
      if self.svs is None:
        self.svs = 0
      if self.sol_svs is None:
        self.sol_svs = 0
      if self.l1_svs is None:
        self.l1_svs = 0
      if self.mult_svs is None:
        self.mult_svs = 0
      if self.reserved is None:
        self.reserved = 0
      if self.extsolstat is None:
        self.extsolstat = 0
      if self.gal_sig_mask is None:
        self.gal_sig_mask = 0
      if self.sig_mask is None:
        self.sig_mask = 0
    else:
      self.header = novatel_msgs.msg.CommonHeader()
      self.solution_status = 0
      self.position_type = 0
      self.latitude = 0.
      self.longitude = 0.
      self.altitude = 0.
      self.undulation = 0.
      self.datum_id = 0
      self.latitude_std = 0.
      self.longitude_std = 0.
      self.altitude_std = 0.
      self.stn_id = chr(0)*4
      self.diff_age = 0.
      self.sol_age = 0.
      self.svs = 0
      self.sol_svs = 0
      self.l1_svs = 0
      self.mult_svs = 0
      self.reserved = 0
      self.extsolstat = 0
      self.gal_sig_mask = 0
      self.sig_mask = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_H2B2H2BH2I2H2I3dfI3f.pack(_x.header.id, _x.header.msg_type, _x.header.port_addr, _x.header.length, _x.header.sequence, _x.header.idle_time, _x.header.time_status, _x.header.gps_week, _x.header.gps_week_seconds, _x.header.receiver_status, _x.header.reserved, _x.header.software_version, _x.solution_status, _x.position_type, _x.latitude, _x.longitude, _x.altitude, _x.undulation, _x.datum_id, _x.latitude_std, _x.longitude_std, _x.altitude_std))
      _x = self.stn_id
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_struct_4B.pack(*_x))
      else:
        buff.write(_struct_4s.pack(_x))
      _x = self
      buff.write(_struct_2f8B.pack(_x.diff_age, _x.sol_age, _x.svs, _x.sol_svs, _x.l1_svs, _x.mult_svs, _x.reserved, _x.extsolstat, _x.gal_sig_mask, _x.sig_mask))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = novatel_msgs.msg.CommonHeader()
      end = 0
      _x = self
      start = end
      end += 76
      (_x.header.id, _x.header.msg_type, _x.header.port_addr, _x.header.length, _x.header.sequence, _x.header.idle_time, _x.header.time_status, _x.header.gps_week, _x.header.gps_week_seconds, _x.header.receiver_status, _x.header.reserved, _x.header.software_version, _x.solution_status, _x.position_type, _x.latitude, _x.longitude, _x.altitude, _x.undulation, _x.datum_id, _x.latitude_std, _x.longitude_std, _x.altitude_std,) = _struct_H2B2H2BH2I2H2I3dfI3f.unpack(str[start:end])
      start = end
      end += 4
      self.stn_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.diff_age, _x.sol_age, _x.svs, _x.sol_svs, _x.l1_svs, _x.mult_svs, _x.reserved, _x.extsolstat, _x.gal_sig_mask, _x.sig_mask,) = _struct_2f8B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_H2B2H2BH2I2H2I3dfI3f.pack(_x.header.id, _x.header.msg_type, _x.header.port_addr, _x.header.length, _x.header.sequence, _x.header.idle_time, _x.header.time_status, _x.header.gps_week, _x.header.gps_week_seconds, _x.header.receiver_status, _x.header.reserved, _x.header.software_version, _x.solution_status, _x.position_type, _x.latitude, _x.longitude, _x.altitude, _x.undulation, _x.datum_id, _x.latitude_std, _x.longitude_std, _x.altitude_std))
      _x = self.stn_id
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_struct_4B.pack(*_x))
      else:
        buff.write(_struct_4s.pack(_x))
      _x = self
      buff.write(_struct_2f8B.pack(_x.diff_age, _x.sol_age, _x.svs, _x.sol_svs, _x.l1_svs, _x.mult_svs, _x.reserved, _x.extsolstat, _x.gal_sig_mask, _x.sig_mask))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = novatel_msgs.msg.CommonHeader()
      end = 0
      _x = self
      start = end
      end += 76
      (_x.header.id, _x.header.msg_type, _x.header.port_addr, _x.header.length, _x.header.sequence, _x.header.idle_time, _x.header.time_status, _x.header.gps_week, _x.header.gps_week_seconds, _x.header.receiver_status, _x.header.reserved, _x.header.software_version, _x.solution_status, _x.position_type, _x.latitude, _x.longitude, _x.altitude, _x.undulation, _x.datum_id, _x.latitude_std, _x.longitude_std, _x.altitude_std,) = _struct_H2B2H2BH2I2H2I3dfI3f.unpack(str[start:end])
      start = end
      end += 4
      self.stn_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.diff_age, _x.sol_age, _x.svs, _x.sol_svs, _x.l1_svs, _x.mult_svs, _x.reserved, _x.extsolstat, _x.gal_sig_mask, _x.sig_mask,) = _struct_2f8B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_H2B2H2BH2I2H2I3dfI3f = struct.Struct("<H2B2H2BH2I2H2I3dfI3f")
_struct_4B = struct.Struct("<4B")
_struct_4s = struct.Struct("<4s")
_struct_2f8B = struct.Struct("<2f8B")
