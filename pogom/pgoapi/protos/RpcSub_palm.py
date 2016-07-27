from palm.palm import ProtoBase, is_string, RepeatedSequence, ProtoValueError

_PB_type = type
_PB_finalizers = []

import RpcEnum_palm

class GetPlayerResponse(ProtoBase):
    _required = []
    _field_map = {'profile': 2, 'unknown1': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['unknown1', 'profile']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_unknown1(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_int32, 'unknown1')
            self._cache[1] = r
        return r

    def _establish_parentage_unknown1(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_unknown1), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_unknown1
                v._pbf_establish_parent_callback = self._establish_parentage_unknown1

    def _set_unknown1(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_unknown1(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field unknown1"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_int32

    def _mod_unknown1(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_int32

    def _del_unknown1(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "unknown1"

    unknown1 = property(_get_unknown1, _set_unknown1, _del_unknown1)

    @property
    def unknown1__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def unknown1__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_unknown1(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_unknown1)


    def _get_profile(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, TYPE_Profile, 'profile')
            self._cache[2] = r
        return r

    def _establish_parentage_profile(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_profile), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_profile
                v._pbf_establish_parent_callback = self._establish_parentage_profile

    def _set_profile(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_profile(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field profile"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = TYPE_Profile

    def _mod_profile(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = TYPE_Profile

    def _del_profile(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "profile"

    profile = property(_get_profile, _set_profile, _del_profile)

    @property
    def profile__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def profile__type(self):
        return TYPE_Profile

    def _finalize_profile(cls):
        if is_string(TYPE_Profile):
            cls._pbf_strings.append(2)
        elif _PB_type(TYPE_Profile) is _PB_type:
            assert issubclass(TYPE_Profile, RepeatedSequence)
            if is_string(TYPE_Profile.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_profile)


TYPE_GetPlayerResponse = GetPlayerResponse
_PB_finalizers.append('GetPlayerResponse')

class Profile(ProtoBase):
    _required = [1]
    _field_map = {'username': 2, 'item_storage': 10, 'unknown12': 12, 'unknown13': 13, 'creation_time': 1, 'currency': 14, 'daily_bonus': 11, 'poke_storage': 9, 'team': 5, 'tutorial': 7, 'avatar': 8}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['creation_time', 'username', 'team', 'tutorial', 'avatar', 'poke_storage', 'item_storage', 'daily_bonus', 'unknown12', 'unknown13', 'currency']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_creation_time(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_int64, 'creation_time')
            self._cache[1] = r
        return r

    def _establish_parentage_creation_time(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_creation_time), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_creation_time
                v._pbf_establish_parent_callback = self._establish_parentage_creation_time

    def _set_creation_time(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_creation_time(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field creation_time"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_int64

    def _mod_creation_time(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_int64

    def _del_creation_time(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "creation_time"

    creation_time = property(_get_creation_time, _set_creation_time, _del_creation_time)

    @property
    def creation_time__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def creation_time__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_creation_time(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_creation_time)


    def _get_username(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_string, 'username')
            self._cache[2] = r
        return r

    def _establish_parentage_username(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_username), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_username
                v._pbf_establish_parent_callback = self._establish_parentage_username

    def _set_username(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_username(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field username"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_string

    def _mod_username(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_string

    def _del_username(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "username"

    username = property(_get_username, _set_username, _del_username)

    @property
    def username__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def username__type(self):
        return ProtoBase.TYPE_string

    def _finalize_username(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_username)


    def _get_team(self):
        if 5 in self._cache:
            r = self._cache[5]
        else:
            r = self._buf_get(5, RpcEnum_palm.TYPE_TeamColor, 'team')
            self._cache[5] = r
        return r

    def _establish_parentage_team(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_team), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_team
                v._pbf_establish_parent_callback = self._establish_parentage_team

    def _set_team(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_team(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field team"
            raise ProtoValueError(list_assign_error)
        self._cache[5] = v
        self._mods[5] = RpcEnum_palm.TYPE_TeamColor

    def _mod_team(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[5] = RpcEnum_palm.TYPE_TeamColor

    def _del_team(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 5 in self._cache:
            del self._cache[5]
        if 5 in self._mods:
            del self._mods[5]
        self._buf_del(5)

    _pb_field_name_5 = "team"

    team = property(_get_team, _set_team, _del_team)

    @property
    def team__exists(self):
        return 5 in self._mods or self._buf_exists(5)

    @property
    def team__type(self):
        return RpcEnum_palm.TYPE_TeamColor

    def _finalize_team(cls):
        if is_string(RpcEnum_palm.TYPE_TeamColor):
            cls._pbf_strings.append(5)
        elif _PB_type(RpcEnum_palm.TYPE_TeamColor) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_TeamColor, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_TeamColor.pb_subtype):
                cls._pbf_strings.append(5)

    _pbf_finalizers.append(_finalize_team)


    def _get_tutorial(self):
        if 7 in self._cache:
            r = self._cache[7]
        else:
            r = self._buf_get(7, ProtoBase.TYPE_bytes, 'tutorial')
            self._cache[7] = r
        return r

    def _establish_parentage_tutorial(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_tutorial), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_tutorial
                v._pbf_establish_parent_callback = self._establish_parentage_tutorial

    def _set_tutorial(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_tutorial(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field tutorial"
            raise ProtoValueError(list_assign_error)
        self._cache[7] = v
        self._mods[7] = ProtoBase.TYPE_bytes

    def _mod_tutorial(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[7] = ProtoBase.TYPE_bytes

    def _del_tutorial(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 7 in self._cache:
            del self._cache[7]
        if 7 in self._mods:
            del self._mods[7]
        self._buf_del(7)

    _pb_field_name_7 = "tutorial"

    tutorial = property(_get_tutorial, _set_tutorial, _del_tutorial)

    @property
    def tutorial__exists(self):
        return 7 in self._mods or self._buf_exists(7)

    @property
    def tutorial__type(self):
        return ProtoBase.TYPE_bytes

    def _finalize_tutorial(cls):
        if is_string(ProtoBase.TYPE_bytes):
            cls._pbf_strings.append(7)
        elif _PB_type(ProtoBase.TYPE_bytes) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bytes, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bytes.pb_subtype):
                cls._pbf_strings.append(7)

    _pbf_finalizers.append(_finalize_tutorial)


    def _get_avatar(self):
        if 8 in self._cache:
            r = self._cache[8]
        else:
            r = self._buf_get(8, TYPE_AvatarDetails, 'avatar')
            self._cache[8] = r
        return r

    def _establish_parentage_avatar(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_avatar), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_avatar
                v._pbf_establish_parent_callback = self._establish_parentage_avatar

    def _set_avatar(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_avatar(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field avatar"
            raise ProtoValueError(list_assign_error)
        self._cache[8] = v
        self._mods[8] = TYPE_AvatarDetails

    def _mod_avatar(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[8] = TYPE_AvatarDetails

    def _del_avatar(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 8 in self._cache:
            del self._cache[8]
        if 8 in self._mods:
            del self._mods[8]
        self._buf_del(8)

    _pb_field_name_8 = "avatar"

    avatar = property(_get_avatar, _set_avatar, _del_avatar)

    @property
    def avatar__exists(self):
        return 8 in self._mods or self._buf_exists(8)

    @property
    def avatar__type(self):
        return TYPE_AvatarDetails

    def _finalize_avatar(cls):
        if is_string(TYPE_AvatarDetails):
            cls._pbf_strings.append(8)
        elif _PB_type(TYPE_AvatarDetails) is _PB_type:
            assert issubclass(TYPE_AvatarDetails, RepeatedSequence)
            if is_string(TYPE_AvatarDetails.pb_subtype):
                cls._pbf_strings.append(8)

    _pbf_finalizers.append(_finalize_avatar)


    def _get_poke_storage(self):
        if 9 in self._cache:
            r = self._cache[9]
        else:
            r = self._buf_get(9, ProtoBase.TYPE_int32, 'poke_storage')
            self._cache[9] = r
        return r

    def _establish_parentage_poke_storage(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_poke_storage), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_poke_storage
                v._pbf_establish_parent_callback = self._establish_parentage_poke_storage

    def _set_poke_storage(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_poke_storage(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field poke_storage"
            raise ProtoValueError(list_assign_error)
        self._cache[9] = v
        self._mods[9] = ProtoBase.TYPE_int32

    def _mod_poke_storage(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[9] = ProtoBase.TYPE_int32

    def _del_poke_storage(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 9 in self._cache:
            del self._cache[9]
        if 9 in self._mods:
            del self._mods[9]
        self._buf_del(9)

    _pb_field_name_9 = "poke_storage"

    poke_storage = property(_get_poke_storage, _set_poke_storage, _del_poke_storage)

    @property
    def poke_storage__exists(self):
        return 9 in self._mods or self._buf_exists(9)

    @property
    def poke_storage__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_poke_storage(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(9)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(9)

    _pbf_finalizers.append(_finalize_poke_storage)


    def _get_item_storage(self):
        if 10 in self._cache:
            r = self._cache[10]
        else:
            r = self._buf_get(10, ProtoBase.TYPE_int32, 'item_storage')
            self._cache[10] = r
        return r

    def _establish_parentage_item_storage(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_item_storage), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_item_storage
                v._pbf_establish_parent_callback = self._establish_parentage_item_storage

    def _set_item_storage(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_item_storage(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field item_storage"
            raise ProtoValueError(list_assign_error)
        self._cache[10] = v
        self._mods[10] = ProtoBase.TYPE_int32

    def _mod_item_storage(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[10] = ProtoBase.TYPE_int32

    def _del_item_storage(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 10 in self._cache:
            del self._cache[10]
        if 10 in self._mods:
            del self._mods[10]
        self._buf_del(10)

    _pb_field_name_10 = "item_storage"

    item_storage = property(_get_item_storage, _set_item_storage, _del_item_storage)

    @property
    def item_storage__exists(self):
        return 10 in self._mods or self._buf_exists(10)

    @property
    def item_storage__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_item_storage(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(10)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(10)

    _pbf_finalizers.append(_finalize_item_storage)


    def _get_daily_bonus(self):
        if 11 in self._cache:
            r = self._cache[11]
        else:
            r = self._buf_get(11, TYPE_DailyBonus, 'daily_bonus')
            self._cache[11] = r
        return r

    def _establish_parentage_daily_bonus(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_daily_bonus), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_daily_bonus
                v._pbf_establish_parent_callback = self._establish_parentage_daily_bonus

    def _set_daily_bonus(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_daily_bonus(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field daily_bonus"
            raise ProtoValueError(list_assign_error)
        self._cache[11] = v
        self._mods[11] = TYPE_DailyBonus

    def _mod_daily_bonus(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[11] = TYPE_DailyBonus

    def _del_daily_bonus(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 11 in self._cache:
            del self._cache[11]
        if 11 in self._mods:
            del self._mods[11]
        self._buf_del(11)

    _pb_field_name_11 = "daily_bonus"

    daily_bonus = property(_get_daily_bonus, _set_daily_bonus, _del_daily_bonus)

    @property
    def daily_bonus__exists(self):
        return 11 in self._mods or self._buf_exists(11)

    @property
    def daily_bonus__type(self):
        return TYPE_DailyBonus

    def _finalize_daily_bonus(cls):
        if is_string(TYPE_DailyBonus):
            cls._pbf_strings.append(11)
        elif _PB_type(TYPE_DailyBonus) is _PB_type:
            assert issubclass(TYPE_DailyBonus, RepeatedSequence)
            if is_string(TYPE_DailyBonus.pb_subtype):
                cls._pbf_strings.append(11)

    _pbf_finalizers.append(_finalize_daily_bonus)


    def _get_unknown12(self):
        if 12 in self._cache:
            r = self._cache[12]
        else:
            r = self._buf_get(12, ProtoBase.TYPE_bytes, 'unknown12')
            self._cache[12] = r
        return r

    def _establish_parentage_unknown12(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_unknown12), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_unknown12
                v._pbf_establish_parent_callback = self._establish_parentage_unknown12

    def _set_unknown12(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_unknown12(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field unknown12"
            raise ProtoValueError(list_assign_error)
        self._cache[12] = v
        self._mods[12] = ProtoBase.TYPE_bytes

    def _mod_unknown12(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[12] = ProtoBase.TYPE_bytes

    def _del_unknown12(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 12 in self._cache:
            del self._cache[12]
        if 12 in self._mods:
            del self._mods[12]
        self._buf_del(12)

    _pb_field_name_12 = "unknown12"

    unknown12 = property(_get_unknown12, _set_unknown12, _del_unknown12)

    @property
    def unknown12__exists(self):
        return 12 in self._mods or self._buf_exists(12)

    @property
    def unknown12__type(self):
        return ProtoBase.TYPE_bytes

    def _finalize_unknown12(cls):
        if is_string(ProtoBase.TYPE_bytes):
            cls._pbf_strings.append(12)
        elif _PB_type(ProtoBase.TYPE_bytes) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bytes, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bytes.pb_subtype):
                cls._pbf_strings.append(12)

    _pbf_finalizers.append(_finalize_unknown12)


    def _get_unknown13(self):
        if 13 in self._cache:
            r = self._cache[13]
        else:
            r = self._buf_get(13, ProtoBase.TYPE_bytes, 'unknown13')
            self._cache[13] = r
        return r

    def _establish_parentage_unknown13(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_unknown13), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_unknown13
                v._pbf_establish_parent_callback = self._establish_parentage_unknown13

    def _set_unknown13(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_unknown13(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field unknown13"
            raise ProtoValueError(list_assign_error)
        self._cache[13] = v
        self._mods[13] = ProtoBase.TYPE_bytes

    def _mod_unknown13(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[13] = ProtoBase.TYPE_bytes

    def _del_unknown13(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 13 in self._cache:
            del self._cache[13]
        if 13 in self._mods:
            del self._mods[13]
        self._buf_del(13)

    _pb_field_name_13 = "unknown13"

    unknown13 = property(_get_unknown13, _set_unknown13, _del_unknown13)

    @property
    def unknown13__exists(self):
        return 13 in self._mods or self._buf_exists(13)

    @property
    def unknown13__type(self):
        return ProtoBase.TYPE_bytes

    def _finalize_unknown13(cls):
        if is_string(ProtoBase.TYPE_bytes):
            cls._pbf_strings.append(13)
        elif _PB_type(ProtoBase.TYPE_bytes) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bytes, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bytes.pb_subtype):
                cls._pbf_strings.append(13)

    _pbf_finalizers.append(_finalize_unknown13)


    class Repeated_currency(RepeatedSequence):
        class pb_subtype(object):
            def __get__(self, instance, cls):
                return TYPE_Currency
        pb_subtype = pb_subtype()


    TYPE_Repeated_currency = Repeated_currency


    @property
    def currency__stream(self):
        if 14 in self._cache:
            def acc(v):
                v_ = lambda: v
                return v_
            return [acc(v) for v in self._cache[14]]
        return self._get_repeated(14, self.TYPE_Repeated_currency, "currency", lazy=True)

    def currency__fast_append(self, value):
        self._append_to_repeated(14, self.TYPE_Repeated_currency, value)

    def _get_currency(self):
        if 14 in self._cache:
            r = self._cache[14]
        else:
            r = self._buf_get(14, self.TYPE_Repeated_currency, 'currency')
            self._cache[14] = r
        return r

    def _establish_parentage_currency(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_currency), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_currency
                v._pbf_establish_parent_callback = self._establish_parentage_currency

    def _set_currency(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_currency(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field currency"
            raise ProtoValueError(list_assign_error)
        self._cache[14] = v
        self._mods[14] = self.TYPE_Repeated_currency

    def _mod_currency(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[14] = self.TYPE_Repeated_currency

    def _del_currency(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 14 in self._cache:
            del self._cache[14]
        if 14 in self._mods:
            del self._mods[14]
        self._buf_del(14)

    _pb_field_name_14 = "currency"

    currency = property(_get_currency, _set_currency, _del_currency)

    @property
    def currency__exists(self):
        return 14 in self._mods or self._buf_exists(14)

    @property
    def currency__type(self):
        return self.TYPE_Repeated_currency

    def _finalize_currency(cls):
        if is_string(cls.TYPE_Repeated_currency):
            cls._pbf_strings.append(14)
        elif _PB_type(cls.TYPE_Repeated_currency) is _PB_type:
            assert issubclass(cls.TYPE_Repeated_currency, RepeatedSequence)
            if is_string(cls.TYPE_Repeated_currency.pb_subtype):
                cls._pbf_strings.append(14)

    _pbf_finalizers.append(_finalize_currency)


TYPE_Profile = Profile
_PB_finalizers.append('Profile')

class DailyBonus(ProtoBase):
    _required = []
    _field_map = {'NextDefenderBonusCollectTimestampMs': 2, 'NextCollectTimestampMs': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['NextCollectTimestampMs', 'NextDefenderBonusCollectTimestampMs']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_NextCollectTimestampMs(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_int64, 'NextCollectTimestampMs')
            self._cache[1] = r
        return r

    def _establish_parentage_NextCollectTimestampMs(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_NextCollectTimestampMs), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_NextCollectTimestampMs
                v._pbf_establish_parent_callback = self._establish_parentage_NextCollectTimestampMs

    def _set_NextCollectTimestampMs(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_NextCollectTimestampMs(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field NextCollectTimestampMs"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_int64

    def _mod_NextCollectTimestampMs(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_int64

    def _del_NextCollectTimestampMs(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "NextCollectTimestampMs"

    NextCollectTimestampMs = property(_get_NextCollectTimestampMs, _set_NextCollectTimestampMs, _del_NextCollectTimestampMs)

    @property
    def NextCollectTimestampMs__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def NextCollectTimestampMs__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_NextCollectTimestampMs(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_NextCollectTimestampMs)


    def _get_NextDefenderBonusCollectTimestampMs(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int64, 'NextDefenderBonusCollectTimestampMs')
            self._cache[2] = r
        return r

    def _establish_parentage_NextDefenderBonusCollectTimestampMs(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_NextDefenderBonusCollectTimestampMs), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_NextDefenderBonusCollectTimestampMs
                v._pbf_establish_parent_callback = self._establish_parentage_NextDefenderBonusCollectTimestampMs

    def _set_NextDefenderBonusCollectTimestampMs(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_NextDefenderBonusCollectTimestampMs(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field NextDefenderBonusCollectTimestampMs"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_int64

    def _mod_NextDefenderBonusCollectTimestampMs(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int64

    def _del_NextDefenderBonusCollectTimestampMs(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "NextDefenderBonusCollectTimestampMs"

    NextDefenderBonusCollectTimestampMs = property(_get_NextDefenderBonusCollectTimestampMs, _set_NextDefenderBonusCollectTimestampMs, _del_NextDefenderBonusCollectTimestampMs)

    @property
    def NextDefenderBonusCollectTimestampMs__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def NextDefenderBonusCollectTimestampMs__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_NextDefenderBonusCollectTimestampMs(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_NextDefenderBonusCollectTimestampMs)


TYPE_DailyBonus = DailyBonus
_PB_finalizers.append('DailyBonus')

class Currency(ProtoBase):
    _required = [1]
    _field_map = {'amount': 2, 'type': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['type', 'amount']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_type(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_string, 'type')
            self._cache[1] = r
        return r

    def _establish_parentage_type(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_type), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_type
                v._pbf_establish_parent_callback = self._establish_parentage_type

    def _set_type(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_type(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field type"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_string

    def _mod_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_string

    def _del_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "type"

    type = property(_get_type, _set_type, _del_type)

    @property
    def type__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def type__type(self):
        return ProtoBase.TYPE_string

    def _finalize_type(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_type)


    def _get_amount(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int32, 'amount')
            self._cache[2] = r
        return r

    def _establish_parentage_amount(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_amount), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_amount
                v._pbf_establish_parent_callback = self._establish_parentage_amount

    def _set_amount(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_amount(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field amount"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_int32

    def _mod_amount(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int32

    def _del_amount(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "amount"

    amount = property(_get_amount, _set_amount, _del_amount)

    @property
    def amount__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def amount__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_amount(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_amount)


TYPE_Currency = Currency
_PB_finalizers.append('Currency')

class AvatarDetails(ProtoBase):
    _required = []
    _field_map = {'unknown2': 2, 'unknown3': 3, 'unknown9': 9, 'unknown10': 10}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['unknown9', 'unknown2', 'unknown3', 'unknown10']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_unknown9(self):
        if 9 in self._cache:
            r = self._cache[9]
        else:
            r = self._buf_get(9, ProtoBase.TYPE_int32, 'unknown9')
            self._cache[9] = r
        return r

    def _establish_parentage_unknown9(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_unknown9), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_unknown9
                v._pbf_establish_parent_callback = self._establish_parentage_unknown9

    def _set_unknown9(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_unknown9(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field unknown9"
            raise ProtoValueError(list_assign_error)
        self._cache[9] = v
        self._mods[9] = ProtoBase.TYPE_int32

    def _mod_unknown9(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[9] = ProtoBase.TYPE_int32

    def _del_unknown9(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 9 in self._cache:
            del self._cache[9]
        if 9 in self._mods:
            del self._mods[9]
        self._buf_del(9)

    _pb_field_name_9 = "unknown9"

    unknown9 = property(_get_unknown9, _set_unknown9, _del_unknown9)

    @property
    def unknown9__exists(self):
        return 9 in self._mods or self._buf_exists(9)

    @property
    def unknown9__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_unknown9(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(9)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(9)

    _pbf_finalizers.append(_finalize_unknown9)


    def _get_unknown2(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int32, 'unknown2')
            self._cache[2] = r
        return r

    def _establish_parentage_unknown2(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_unknown2), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_unknown2
                v._pbf_establish_parent_callback = self._establish_parentage_unknown2

    def _set_unknown2(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_unknown2(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field unknown2"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_int32

    def _mod_unknown2(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int32

    def _del_unknown2(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "unknown2"

    unknown2 = property(_get_unknown2, _set_unknown2, _del_unknown2)

    @property
    def unknown2__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def unknown2__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_unknown2(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_unknown2)


    def _get_unknown3(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_int32, 'unknown3')
            self._cache[3] = r
        return r

    def _establish_parentage_unknown3(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_unknown3), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_unknown3
                v._pbf_establish_parent_callback = self._establish_parentage_unknown3

    def _set_unknown3(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_unknown3(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field unknown3"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_int32

    def _mod_unknown3(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_int32

    def _del_unknown3(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "unknown3"

    unknown3 = property(_get_unknown3, _set_unknown3, _del_unknown3)

    @property
    def unknown3__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def unknown3__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_unknown3(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_unknown3)


    def _get_unknown10(self):
        if 10 in self._cache:
            r = self._cache[10]
        else:
            r = self._buf_get(10, ProtoBase.TYPE_int32, 'unknown10')
            self._cache[10] = r
        return r

    def _establish_parentage_unknown10(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_unknown10), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_unknown10
                v._pbf_establish_parent_callback = self._establish_parentage_unknown10

    def _set_unknown10(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_unknown10(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field unknown10"
            raise ProtoValueError(list_assign_error)
        self._cache[10] = v
        self._mods[10] = ProtoBase.TYPE_int32

    def _mod_unknown10(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[10] = ProtoBase.TYPE_int32

    def _del_unknown10(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 10 in self._cache:
            del self._cache[10]
        if 10 in self._mods:
            del self._mods[10]
        self._buf_del(10)

    _pb_field_name_10 = "unknown10"

    unknown10 = property(_get_unknown10, _set_unknown10, _del_unknown10)

    @property
    def unknown10__exists(self):
        return 10 in self._mods or self._buf_exists(10)

    @property
    def unknown10__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_unknown10(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(10)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(10)

    _pbf_finalizers.append(_finalize_unknown10)


TYPE_AvatarDetails = AvatarDetails
_PB_finalizers.append('AvatarDetails')

class DownloadSettingsRequest(ProtoBase):
    _required = []
    _field_map = {'hash': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['hash']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_hash(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_string, 'hash')
            self._cache[1] = r
        return r

    def _establish_parentage_hash(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_hash), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_hash
                v._pbf_establish_parent_callback = self._establish_parentage_hash

    def _set_hash(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_hash(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field hash"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_string

    def _mod_hash(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_string

    def _del_hash(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "hash"

    hash = property(_get_hash, _set_hash, _del_hash)

    @property
    def hash__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def hash__type(self):
        return ProtoBase.TYPE_string

    def _finalize_hash(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_hash)


TYPE_DownloadSettingsRequest = DownloadSettingsRequest
_PB_finalizers.append('DownloadSettingsRequest')

class GetInventoryResponse(ProtoBase):
    _required = []
    _field_map = {'inventory_delta': 2, 'success': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['success', 'inventory_delta']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_success(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_bool, 'success')
            self._cache[1] = r
        return r

    def _establish_parentage_success(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_success), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_success
                v._pbf_establish_parent_callback = self._establish_parentage_success

    def _set_success(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_success(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field success"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_bool

    def _mod_success(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_bool

    def _del_success(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "success"

    success = property(_get_success, _set_success, _del_success)

    @property
    def success__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def success__type(self):
        return ProtoBase.TYPE_bool

    def _finalize_success(cls):
        if is_string(ProtoBase.TYPE_bool):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_bool) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bool, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bool.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_success)


    def _get_inventory_delta(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, TYPE_InventoryDelta, 'inventory_delta')
            self._cache[2] = r
        return r

    def _establish_parentage_inventory_delta(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_inventory_delta), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_inventory_delta
                v._pbf_establish_parent_callback = self._establish_parentage_inventory_delta

    def _set_inventory_delta(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_inventory_delta(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field inventory_delta"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = TYPE_InventoryDelta

    def _mod_inventory_delta(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = TYPE_InventoryDelta

    def _del_inventory_delta(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "inventory_delta"

    inventory_delta = property(_get_inventory_delta, _set_inventory_delta, _del_inventory_delta)

    @property
    def inventory_delta__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def inventory_delta__type(self):
        return TYPE_InventoryDelta

    def _finalize_inventory_delta(cls):
        if is_string(TYPE_InventoryDelta):
            cls._pbf_strings.append(2)
        elif _PB_type(TYPE_InventoryDelta) is _PB_type:
            assert issubclass(TYPE_InventoryDelta, RepeatedSequence)
            if is_string(TYPE_InventoryDelta.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_inventory_delta)


TYPE_GetInventoryResponse = GetInventoryResponse
_PB_finalizers.append('GetInventoryResponse')

class InventoryDelta(ProtoBase):
    _required = []
    _field_map = {'inventory_items': 3, 'new_timestamp_ms': 2, 'original_timestamp_ms': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['original_timestamp_ms', 'new_timestamp_ms', 'inventory_items']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_original_timestamp_ms(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_int64, 'original_timestamp_ms')
            self._cache[1] = r
        return r

    def _establish_parentage_original_timestamp_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_original_timestamp_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_original_timestamp_ms
                v._pbf_establish_parent_callback = self._establish_parentage_original_timestamp_ms

    def _set_original_timestamp_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_original_timestamp_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field original_timestamp_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_int64

    def _mod_original_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_int64

    def _del_original_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "original_timestamp_ms"

    original_timestamp_ms = property(_get_original_timestamp_ms, _set_original_timestamp_ms, _del_original_timestamp_ms)

    @property
    def original_timestamp_ms__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def original_timestamp_ms__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_original_timestamp_ms(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_original_timestamp_ms)


    def _get_new_timestamp_ms(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int64, 'new_timestamp_ms')
            self._cache[2] = r
        return r

    def _establish_parentage_new_timestamp_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_new_timestamp_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_new_timestamp_ms
                v._pbf_establish_parent_callback = self._establish_parentage_new_timestamp_ms

    def _set_new_timestamp_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_new_timestamp_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field new_timestamp_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_int64

    def _mod_new_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int64

    def _del_new_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "new_timestamp_ms"

    new_timestamp_ms = property(_get_new_timestamp_ms, _set_new_timestamp_ms, _del_new_timestamp_ms)

    @property
    def new_timestamp_ms__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def new_timestamp_ms__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_new_timestamp_ms(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_new_timestamp_ms)


    class Repeated_inventory_items(RepeatedSequence):
        class pb_subtype(object):
            def __get__(self, instance, cls):
                return TYPE_InventoryItem
        pb_subtype = pb_subtype()


    TYPE_Repeated_inventory_items = Repeated_inventory_items


    @property
    def inventory_items__stream(self):
        if 3 in self._cache:
            def acc(v):
                v_ = lambda: v
                return v_
            return [acc(v) for v in self._cache[3]]
        return self._get_repeated(3, self.TYPE_Repeated_inventory_items, "inventory_items", lazy=True)

    def inventory_items__fast_append(self, value):
        self._append_to_repeated(3, self.TYPE_Repeated_inventory_items, value)

    def _get_inventory_items(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, self.TYPE_Repeated_inventory_items, 'inventory_items')
            self._cache[3] = r
        return r

    def _establish_parentage_inventory_items(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_inventory_items), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_inventory_items
                v._pbf_establish_parent_callback = self._establish_parentage_inventory_items

    def _set_inventory_items(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_inventory_items(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field inventory_items"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = self.TYPE_Repeated_inventory_items

    def _mod_inventory_items(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = self.TYPE_Repeated_inventory_items

    def _del_inventory_items(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "inventory_items"

    inventory_items = property(_get_inventory_items, _set_inventory_items, _del_inventory_items)

    @property
    def inventory_items__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def inventory_items__type(self):
        return self.TYPE_Repeated_inventory_items

    def _finalize_inventory_items(cls):
        if is_string(cls.TYPE_Repeated_inventory_items):
            cls._pbf_strings.append(3)
        elif _PB_type(cls.TYPE_Repeated_inventory_items) is _PB_type:
            assert issubclass(cls.TYPE_Repeated_inventory_items, RepeatedSequence)
            if is_string(cls.TYPE_Repeated_inventory_items.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_inventory_items)


TYPE_InventoryDelta = InventoryDelta
_PB_finalizers.append('InventoryDelta')

class InventoryItem(ProtoBase):
    _required = []
    _field_map = {'inventory_item_data': 3, 'modified_timestamp_ms': 1, 'deleted_item_key': 2}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['modified_timestamp_ms', 'deleted_item_key', 'inventory_item_data']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_modified_timestamp_ms(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_int64, 'modified_timestamp_ms')
            self._cache[1] = r
        return r

    def _establish_parentage_modified_timestamp_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_modified_timestamp_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_modified_timestamp_ms
                v._pbf_establish_parent_callback = self._establish_parentage_modified_timestamp_ms

    def _set_modified_timestamp_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_modified_timestamp_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field modified_timestamp_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_int64

    def _mod_modified_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_int64

    def _del_modified_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "modified_timestamp_ms"

    modified_timestamp_ms = property(_get_modified_timestamp_ms, _set_modified_timestamp_ms, _del_modified_timestamp_ms)

    @property
    def modified_timestamp_ms__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def modified_timestamp_ms__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_modified_timestamp_ms(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_modified_timestamp_ms)


    def _get_deleted_item_key(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int64, 'deleted_item_key')
            self._cache[2] = r
        return r

    def _establish_parentage_deleted_item_key(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_deleted_item_key), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_deleted_item_key
                v._pbf_establish_parent_callback = self._establish_parentage_deleted_item_key

    def _set_deleted_item_key(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_deleted_item_key(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field deleted_item_key"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_int64

    def _mod_deleted_item_key(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int64

    def _del_deleted_item_key(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "deleted_item_key"

    deleted_item_key = property(_get_deleted_item_key, _set_deleted_item_key, _del_deleted_item_key)

    @property
    def deleted_item_key__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def deleted_item_key__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_deleted_item_key(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_deleted_item_key)


    def _get_inventory_item_data(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, TYPE_InventoryItemData, 'inventory_item_data')
            self._cache[3] = r
        return r

    def _establish_parentage_inventory_item_data(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_inventory_item_data), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_inventory_item_data
                v._pbf_establish_parent_callback = self._establish_parentage_inventory_item_data

    def _set_inventory_item_data(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_inventory_item_data(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field inventory_item_data"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = TYPE_InventoryItemData

    def _mod_inventory_item_data(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = TYPE_InventoryItemData

    def _del_inventory_item_data(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "inventory_item_data"

    inventory_item_data = property(_get_inventory_item_data, _set_inventory_item_data, _del_inventory_item_data)

    @property
    def inventory_item_data__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def inventory_item_data__type(self):
        return TYPE_InventoryItemData

    def _finalize_inventory_item_data(cls):
        if is_string(TYPE_InventoryItemData):
            cls._pbf_strings.append(3)
        elif _PB_type(TYPE_InventoryItemData) is _PB_type:
            assert issubclass(TYPE_InventoryItemData, RepeatedSequence)
            if is_string(TYPE_InventoryItemData.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_inventory_item_data)


TYPE_InventoryItem = InventoryItem
_PB_finalizers.append('InventoryItem')

class InventoryItemData(ProtoBase):
    _required = []
    _field_map = {'player_camera': 6, 'egg_incubators': 9, 'inventory_upgrades': 7, 'item': 2, 'pokedex_entry': 3, 'applied_items': 8, 'pokemon_family': 10, 'player_currency': 5, 'player_stats': 4, 'pokemon': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['pokemon', 'item', 'pokedex_entry', 'player_stats', 'player_currency', 'player_camera', 'inventory_upgrades', 'applied_items', 'egg_incubators', 'pokemon_family']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_pokemon(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, TYPE_Pokemon, 'pokemon')
            self._cache[1] = r
        return r

    def _establish_parentage_pokemon(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokemon), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokemon
                v._pbf_establish_parent_callback = self._establish_parentage_pokemon

    def _set_pokemon(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokemon(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokemon"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = TYPE_Pokemon

    def _mod_pokemon(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = TYPE_Pokemon

    def _del_pokemon(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "pokemon"

    pokemon = property(_get_pokemon, _set_pokemon, _del_pokemon)

    @property
    def pokemon__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def pokemon__type(self):
        return TYPE_Pokemon

    def _finalize_pokemon(cls):
        if is_string(TYPE_Pokemon):
            cls._pbf_strings.append(1)
        elif _PB_type(TYPE_Pokemon) is _PB_type:
            assert issubclass(TYPE_Pokemon, RepeatedSequence)
            if is_string(TYPE_Pokemon.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_pokemon)


    def _get_item(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, TYPE_Item, 'item')
            self._cache[2] = r
        return r

    def _establish_parentage_item(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_item), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_item
                v._pbf_establish_parent_callback = self._establish_parentage_item

    def _set_item(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_item(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field item"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = TYPE_Item

    def _mod_item(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = TYPE_Item

    def _del_item(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "item"

    item = property(_get_item, _set_item, _del_item)

    @property
    def item__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def item__type(self):
        return TYPE_Item

    def _finalize_item(cls):
        if is_string(TYPE_Item):
            cls._pbf_strings.append(2)
        elif _PB_type(TYPE_Item) is _PB_type:
            assert issubclass(TYPE_Item, RepeatedSequence)
            if is_string(TYPE_Item.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_item)


    def _get_pokedex_entry(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, TYPE_PokedexEntry, 'pokedex_entry')
            self._cache[3] = r
        return r

    def _establish_parentage_pokedex_entry(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokedex_entry), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokedex_entry
                v._pbf_establish_parent_callback = self._establish_parentage_pokedex_entry

    def _set_pokedex_entry(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokedex_entry(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokedex_entry"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = TYPE_PokedexEntry

    def _mod_pokedex_entry(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = TYPE_PokedexEntry

    def _del_pokedex_entry(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "pokedex_entry"

    pokedex_entry = property(_get_pokedex_entry, _set_pokedex_entry, _del_pokedex_entry)

    @property
    def pokedex_entry__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def pokedex_entry__type(self):
        return TYPE_PokedexEntry

    def _finalize_pokedex_entry(cls):
        if is_string(TYPE_PokedexEntry):
            cls._pbf_strings.append(3)
        elif _PB_type(TYPE_PokedexEntry) is _PB_type:
            assert issubclass(TYPE_PokedexEntry, RepeatedSequence)
            if is_string(TYPE_PokedexEntry.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_pokedex_entry)


    def _get_player_stats(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, TYPE_PlayerStats, 'player_stats')
            self._cache[4] = r
        return r

    def _establish_parentage_player_stats(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_player_stats), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_player_stats
                v._pbf_establish_parent_callback = self._establish_parentage_player_stats

    def _set_player_stats(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_player_stats(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field player_stats"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = TYPE_PlayerStats

    def _mod_player_stats(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = TYPE_PlayerStats

    def _del_player_stats(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "player_stats"

    player_stats = property(_get_player_stats, _set_player_stats, _del_player_stats)

    @property
    def player_stats__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def player_stats__type(self):
        return TYPE_PlayerStats

    def _finalize_player_stats(cls):
        if is_string(TYPE_PlayerStats):
            cls._pbf_strings.append(4)
        elif _PB_type(TYPE_PlayerStats) is _PB_type:
            assert issubclass(TYPE_PlayerStats, RepeatedSequence)
            if is_string(TYPE_PlayerStats.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_player_stats)


    def _get_player_currency(self):
        if 5 in self._cache:
            r = self._cache[5]
        else:
            r = self._buf_get(5, TYPE_PlayerCurrency, 'player_currency')
            self._cache[5] = r
        return r

    def _establish_parentage_player_currency(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_player_currency), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_player_currency
                v._pbf_establish_parent_callback = self._establish_parentage_player_currency

    def _set_player_currency(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_player_currency(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field player_currency"
            raise ProtoValueError(list_assign_error)
        self._cache[5] = v
        self._mods[5] = TYPE_PlayerCurrency

    def _mod_player_currency(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[5] = TYPE_PlayerCurrency

    def _del_player_currency(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 5 in self._cache:
            del self._cache[5]
        if 5 in self._mods:
            del self._mods[5]
        self._buf_del(5)

    _pb_field_name_5 = "player_currency"

    player_currency = property(_get_player_currency, _set_player_currency, _del_player_currency)

    @property
    def player_currency__exists(self):
        return 5 in self._mods or self._buf_exists(5)

    @property
    def player_currency__type(self):
        return TYPE_PlayerCurrency

    def _finalize_player_currency(cls):
        if is_string(TYPE_PlayerCurrency):
            cls._pbf_strings.append(5)
        elif _PB_type(TYPE_PlayerCurrency) is _PB_type:
            assert issubclass(TYPE_PlayerCurrency, RepeatedSequence)
            if is_string(TYPE_PlayerCurrency.pb_subtype):
                cls._pbf_strings.append(5)

    _pbf_finalizers.append(_finalize_player_currency)


    def _get_player_camera(self):
        if 6 in self._cache:
            r = self._cache[6]
        else:
            r = self._buf_get(6, TYPE_PlayerCamera, 'player_camera')
            self._cache[6] = r
        return r

    def _establish_parentage_player_camera(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_player_camera), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_player_camera
                v._pbf_establish_parent_callback = self._establish_parentage_player_camera

    def _set_player_camera(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_player_camera(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field player_camera"
            raise ProtoValueError(list_assign_error)
        self._cache[6] = v
        self._mods[6] = TYPE_PlayerCamera

    def _mod_player_camera(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[6] = TYPE_PlayerCamera

    def _del_player_camera(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 6 in self._cache:
            del self._cache[6]
        if 6 in self._mods:
            del self._mods[6]
        self._buf_del(6)

    _pb_field_name_6 = "player_camera"

    player_camera = property(_get_player_camera, _set_player_camera, _del_player_camera)

    @property
    def player_camera__exists(self):
        return 6 in self._mods or self._buf_exists(6)

    @property
    def player_camera__type(self):
        return TYPE_PlayerCamera

    def _finalize_player_camera(cls):
        if is_string(TYPE_PlayerCamera):
            cls._pbf_strings.append(6)
        elif _PB_type(TYPE_PlayerCamera) is _PB_type:
            assert issubclass(TYPE_PlayerCamera, RepeatedSequence)
            if is_string(TYPE_PlayerCamera.pb_subtype):
                cls._pbf_strings.append(6)

    _pbf_finalizers.append(_finalize_player_camera)


    def _get_inventory_upgrades(self):
        if 7 in self._cache:
            r = self._cache[7]
        else:
            r = self._buf_get(7, TYPE_InventoryUpgrades, 'inventory_upgrades')
            self._cache[7] = r
        return r

    def _establish_parentage_inventory_upgrades(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_inventory_upgrades), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_inventory_upgrades
                v._pbf_establish_parent_callback = self._establish_parentage_inventory_upgrades

    def _set_inventory_upgrades(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_inventory_upgrades(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field inventory_upgrades"
            raise ProtoValueError(list_assign_error)
        self._cache[7] = v
        self._mods[7] = TYPE_InventoryUpgrades

    def _mod_inventory_upgrades(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[7] = TYPE_InventoryUpgrades

    def _del_inventory_upgrades(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 7 in self._cache:
            del self._cache[7]
        if 7 in self._mods:
            del self._mods[7]
        self._buf_del(7)

    _pb_field_name_7 = "inventory_upgrades"

    inventory_upgrades = property(_get_inventory_upgrades, _set_inventory_upgrades, _del_inventory_upgrades)

    @property
    def inventory_upgrades__exists(self):
        return 7 in self._mods or self._buf_exists(7)

    @property
    def inventory_upgrades__type(self):
        return TYPE_InventoryUpgrades

    def _finalize_inventory_upgrades(cls):
        if is_string(TYPE_InventoryUpgrades):
            cls._pbf_strings.append(7)
        elif _PB_type(TYPE_InventoryUpgrades) is _PB_type:
            assert issubclass(TYPE_InventoryUpgrades, RepeatedSequence)
            if is_string(TYPE_InventoryUpgrades.pb_subtype):
                cls._pbf_strings.append(7)

    _pbf_finalizers.append(_finalize_inventory_upgrades)


    def _get_applied_items(self):
        if 8 in self._cache:
            r = self._cache[8]
        else:
            r = self._buf_get(8, TYPE_AppliedItems, 'applied_items')
            self._cache[8] = r
        return r

    def _establish_parentage_applied_items(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_applied_items), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_applied_items
                v._pbf_establish_parent_callback = self._establish_parentage_applied_items

    def _set_applied_items(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_applied_items(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field applied_items"
            raise ProtoValueError(list_assign_error)
        self._cache[8] = v
        self._mods[8] = TYPE_AppliedItems

    def _mod_applied_items(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[8] = TYPE_AppliedItems

    def _del_applied_items(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 8 in self._cache:
            del self._cache[8]
        if 8 in self._mods:
            del self._mods[8]
        self._buf_del(8)

    _pb_field_name_8 = "applied_items"

    applied_items = property(_get_applied_items, _set_applied_items, _del_applied_items)

    @property
    def applied_items__exists(self):
        return 8 in self._mods or self._buf_exists(8)

    @property
    def applied_items__type(self):
        return TYPE_AppliedItems

    def _finalize_applied_items(cls):
        if is_string(TYPE_AppliedItems):
            cls._pbf_strings.append(8)
        elif _PB_type(TYPE_AppliedItems) is _PB_type:
            assert issubclass(TYPE_AppliedItems, RepeatedSequence)
            if is_string(TYPE_AppliedItems.pb_subtype):
                cls._pbf_strings.append(8)

    _pbf_finalizers.append(_finalize_applied_items)


    def _get_egg_incubators(self):
        if 9 in self._cache:
            r = self._cache[9]
        else:
            r = self._buf_get(9, TYPE_EggIncubators, 'egg_incubators')
            self._cache[9] = r
        return r

    def _establish_parentage_egg_incubators(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_egg_incubators), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_egg_incubators
                v._pbf_establish_parent_callback = self._establish_parentage_egg_incubators

    def _set_egg_incubators(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_egg_incubators(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field egg_incubators"
            raise ProtoValueError(list_assign_error)
        self._cache[9] = v
        self._mods[9] = TYPE_EggIncubators

    def _mod_egg_incubators(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[9] = TYPE_EggIncubators

    def _del_egg_incubators(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 9 in self._cache:
            del self._cache[9]
        if 9 in self._mods:
            del self._mods[9]
        self._buf_del(9)

    _pb_field_name_9 = "egg_incubators"

    egg_incubators = property(_get_egg_incubators, _set_egg_incubators, _del_egg_incubators)

    @property
    def egg_incubators__exists(self):
        return 9 in self._mods or self._buf_exists(9)

    @property
    def egg_incubators__type(self):
        return TYPE_EggIncubators

    def _finalize_egg_incubators(cls):
        if is_string(TYPE_EggIncubators):
            cls._pbf_strings.append(9)
        elif _PB_type(TYPE_EggIncubators) is _PB_type:
            assert issubclass(TYPE_EggIncubators, RepeatedSequence)
            if is_string(TYPE_EggIncubators.pb_subtype):
                cls._pbf_strings.append(9)

    _pbf_finalizers.append(_finalize_egg_incubators)


    def _get_pokemon_family(self):
        if 10 in self._cache:
            r = self._cache[10]
        else:
            r = self._buf_get(10, TYPE_PokemonFamily, 'pokemon_family')
            self._cache[10] = r
        return r

    def _establish_parentage_pokemon_family(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokemon_family), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokemon_family
                v._pbf_establish_parent_callback = self._establish_parentage_pokemon_family

    def _set_pokemon_family(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokemon_family(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokemon_family"
            raise ProtoValueError(list_assign_error)
        self._cache[10] = v
        self._mods[10] = TYPE_PokemonFamily

    def _mod_pokemon_family(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[10] = TYPE_PokemonFamily

    def _del_pokemon_family(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 10 in self._cache:
            del self._cache[10]
        if 10 in self._mods:
            del self._mods[10]
        self._buf_del(10)

    _pb_field_name_10 = "pokemon_family"

    pokemon_family = property(_get_pokemon_family, _set_pokemon_family, _del_pokemon_family)

    @property
    def pokemon_family__exists(self):
        return 10 in self._mods or self._buf_exists(10)

    @property
    def pokemon_family__type(self):
        return TYPE_PokemonFamily

    def _finalize_pokemon_family(cls):
        if is_string(TYPE_PokemonFamily):
            cls._pbf_strings.append(10)
        elif _PB_type(TYPE_PokemonFamily) is _PB_type:
            assert issubclass(TYPE_PokemonFamily, RepeatedSequence)
            if is_string(TYPE_PokemonFamily.pb_subtype):
                cls._pbf_strings.append(10)

    _pbf_finalizers.append(_finalize_pokemon_family)


TYPE_InventoryItemData = InventoryItemData
_PB_finalizers.append('InventoryItemData')

class Pokemon(ProtoBase):
    _required = []
    _field_map = {'origin': 14, 'is_egg': 10, 'egg_km_walked_target': 11, 'creation_time_ms': 26, 'cp_multiplier': 20, 'cp': 3, 'id': 1, 'move_1': 6, 'pokemon_type': 2, 'individual_stamina': 19, 'stamina': 4, 'individual_attack': 17, 'owner_name': 9, 'stamina_max': 5, 'weight_kg': 16, 'move_2': 7, 'battles_attacked': 23, 'nickname': 30, 'from_fort': 31, 'num_upgrades': 27, 'individual_defense': 18, 'additional_cp_multiplier': 28, 'pokeball': 21, 'egg_incubator_id': 25, 'height_m': 15, 'captured_cell_id': 22, 'favorite': 29, 'egg_km_walked_start': 12, 'battles_defended': 24, 'deployed_fort_id': 8}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['id', 'pokemon_type', 'cp', 'stamina', 'stamina_max', 'move_1', 'move_2', 'deployed_fort_id', 'owner_name', 'is_egg', 'egg_km_walked_target', 'egg_km_walked_start', 'origin', 'height_m', 'weight_kg', 'individual_attack', 'individual_defense', 'individual_stamina', 'cp_multiplier', 'pokeball', 'captured_cell_id', 'battles_attacked', 'battles_defended', 'egg_incubator_id', 'creation_time_ms', 'num_upgrades', 'additional_cp_multiplier', 'favorite', 'nickname', 'from_fort']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_id(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_int32, 'id')
            self._cache[1] = r
        return r

    def _establish_parentage_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_id
                v._pbf_establish_parent_callback = self._establish_parentage_id

    def _set_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field id"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_int32

    def _mod_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_int32

    def _del_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "id"

    id = property(_get_id, _set_id, _del_id)

    @property
    def id__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def id__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_id(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_id)


    def _get_pokemon_type(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, RpcEnum_palm.TYPE_PokemonId, 'pokemon_type')
            self._cache[2] = r
        return r

    def _establish_parentage_pokemon_type(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokemon_type), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokemon_type
                v._pbf_establish_parent_callback = self._establish_parentage_pokemon_type

    def _set_pokemon_type(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokemon_type(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokemon_type"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = RpcEnum_palm.TYPE_PokemonId

    def _mod_pokemon_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = RpcEnum_palm.TYPE_PokemonId

    def _del_pokemon_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "pokemon_type"

    pokemon_type = property(_get_pokemon_type, _set_pokemon_type, _del_pokemon_type)

    @property
    def pokemon_type__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def pokemon_type__type(self):
        return RpcEnum_palm.TYPE_PokemonId

    def _finalize_pokemon_type(cls):
        if is_string(RpcEnum_palm.TYPE_PokemonId):
            cls._pbf_strings.append(2)
        elif _PB_type(RpcEnum_palm.TYPE_PokemonId) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_PokemonId, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_PokemonId.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_pokemon_type)


    def _get_cp(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_int32, 'cp')
            self._cache[3] = r
        return r

    def _establish_parentage_cp(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_cp), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_cp
                v._pbf_establish_parent_callback = self._establish_parentage_cp

    def _set_cp(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_cp(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field cp"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_int32

    def _mod_cp(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_int32

    def _del_cp(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "cp"

    cp = property(_get_cp, _set_cp, _del_cp)

    @property
    def cp__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def cp__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_cp(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_cp)


    def _get_stamina(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, ProtoBase.TYPE_int32, 'stamina')
            self._cache[4] = r
        return r

    def _establish_parentage_stamina(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_stamina), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_stamina
                v._pbf_establish_parent_callback = self._establish_parentage_stamina

    def _set_stamina(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_stamina(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field stamina"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = ProtoBase.TYPE_int32

    def _mod_stamina(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = ProtoBase.TYPE_int32

    def _del_stamina(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "stamina"

    stamina = property(_get_stamina, _set_stamina, _del_stamina)

    @property
    def stamina__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def stamina__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_stamina(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(4)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_stamina)


    def _get_stamina_max(self):
        if 5 in self._cache:
            r = self._cache[5]
        else:
            r = self._buf_get(5, ProtoBase.TYPE_int32, 'stamina_max')
            self._cache[5] = r
        return r

    def _establish_parentage_stamina_max(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_stamina_max), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_stamina_max
                v._pbf_establish_parent_callback = self._establish_parentage_stamina_max

    def _set_stamina_max(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_stamina_max(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field stamina_max"
            raise ProtoValueError(list_assign_error)
        self._cache[5] = v
        self._mods[5] = ProtoBase.TYPE_int32

    def _mod_stamina_max(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[5] = ProtoBase.TYPE_int32

    def _del_stamina_max(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 5 in self._cache:
            del self._cache[5]
        if 5 in self._mods:
            del self._mods[5]
        self._buf_del(5)

    _pb_field_name_5 = "stamina_max"

    stamina_max = property(_get_stamina_max, _set_stamina_max, _del_stamina_max)

    @property
    def stamina_max__exists(self):
        return 5 in self._mods or self._buf_exists(5)

    @property
    def stamina_max__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_stamina_max(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(5)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(5)

    _pbf_finalizers.append(_finalize_stamina_max)


    def _get_move_1(self):
        if 6 in self._cache:
            r = self._cache[6]
        else:
            r = self._buf_get(6, RpcEnum_palm.TYPE_PokemonMove, 'move_1')
            self._cache[6] = r
        return r

    def _establish_parentage_move_1(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_move_1), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_move_1
                v._pbf_establish_parent_callback = self._establish_parentage_move_1

    def _set_move_1(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_move_1(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field move_1"
            raise ProtoValueError(list_assign_error)
        self._cache[6] = v
        self._mods[6] = RpcEnum_palm.TYPE_PokemonMove

    def _mod_move_1(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[6] = RpcEnum_palm.TYPE_PokemonMove

    def _del_move_1(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 6 in self._cache:
            del self._cache[6]
        if 6 in self._mods:
            del self._mods[6]
        self._buf_del(6)

    _pb_field_name_6 = "move_1"

    move_1 = property(_get_move_1, _set_move_1, _del_move_1)

    @property
    def move_1__exists(self):
        return 6 in self._mods or self._buf_exists(6)

    @property
    def move_1__type(self):
        return RpcEnum_palm.TYPE_PokemonMove

    def _finalize_move_1(cls):
        if is_string(RpcEnum_palm.TYPE_PokemonMove):
            cls._pbf_strings.append(6)
        elif _PB_type(RpcEnum_palm.TYPE_PokemonMove) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_PokemonMove, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_PokemonMove.pb_subtype):
                cls._pbf_strings.append(6)

    _pbf_finalizers.append(_finalize_move_1)


    def _get_move_2(self):
        if 7 in self._cache:
            r = self._cache[7]
        else:
            r = self._buf_get(7, RpcEnum_palm.TYPE_PokemonMove, 'move_2')
            self._cache[7] = r
        return r

    def _establish_parentage_move_2(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_move_2), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_move_2
                v._pbf_establish_parent_callback = self._establish_parentage_move_2

    def _set_move_2(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_move_2(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field move_2"
            raise ProtoValueError(list_assign_error)
        self._cache[7] = v
        self._mods[7] = RpcEnum_palm.TYPE_PokemonMove

    def _mod_move_2(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[7] = RpcEnum_palm.TYPE_PokemonMove

    def _del_move_2(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 7 in self._cache:
            del self._cache[7]
        if 7 in self._mods:
            del self._mods[7]
        self._buf_del(7)

    _pb_field_name_7 = "move_2"

    move_2 = property(_get_move_2, _set_move_2, _del_move_2)

    @property
    def move_2__exists(self):
        return 7 in self._mods or self._buf_exists(7)

    @property
    def move_2__type(self):
        return RpcEnum_palm.TYPE_PokemonMove

    def _finalize_move_2(cls):
        if is_string(RpcEnum_palm.TYPE_PokemonMove):
            cls._pbf_strings.append(7)
        elif _PB_type(RpcEnum_palm.TYPE_PokemonMove) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_PokemonMove, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_PokemonMove.pb_subtype):
                cls._pbf_strings.append(7)

    _pbf_finalizers.append(_finalize_move_2)


    def _get_deployed_fort_id(self):
        if 8 in self._cache:
            r = self._cache[8]
        else:
            r = self._buf_get(8, ProtoBase.TYPE_int32, 'deployed_fort_id')
            self._cache[8] = r
        return r

    def _establish_parentage_deployed_fort_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_deployed_fort_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_deployed_fort_id
                v._pbf_establish_parent_callback = self._establish_parentage_deployed_fort_id

    def _set_deployed_fort_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_deployed_fort_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field deployed_fort_id"
            raise ProtoValueError(list_assign_error)
        self._cache[8] = v
        self._mods[8] = ProtoBase.TYPE_int32

    def _mod_deployed_fort_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[8] = ProtoBase.TYPE_int32

    def _del_deployed_fort_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 8 in self._cache:
            del self._cache[8]
        if 8 in self._mods:
            del self._mods[8]
        self._buf_del(8)

    _pb_field_name_8 = "deployed_fort_id"

    deployed_fort_id = property(_get_deployed_fort_id, _set_deployed_fort_id, _del_deployed_fort_id)

    @property
    def deployed_fort_id__exists(self):
        return 8 in self._mods or self._buf_exists(8)

    @property
    def deployed_fort_id__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_deployed_fort_id(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(8)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(8)

    _pbf_finalizers.append(_finalize_deployed_fort_id)


    def _get_owner_name(self):
        if 9 in self._cache:
            r = self._cache[9]
        else:
            r = self._buf_get(9, ProtoBase.TYPE_string, 'owner_name')
            self._cache[9] = r
        return r

    def _establish_parentage_owner_name(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_owner_name), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_owner_name
                v._pbf_establish_parent_callback = self._establish_parentage_owner_name

    def _set_owner_name(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_owner_name(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field owner_name"
            raise ProtoValueError(list_assign_error)
        self._cache[9] = v
        self._mods[9] = ProtoBase.TYPE_string

    def _mod_owner_name(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[9] = ProtoBase.TYPE_string

    def _del_owner_name(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 9 in self._cache:
            del self._cache[9]
        if 9 in self._mods:
            del self._mods[9]
        self._buf_del(9)

    _pb_field_name_9 = "owner_name"

    owner_name = property(_get_owner_name, _set_owner_name, _del_owner_name)

    @property
    def owner_name__exists(self):
        return 9 in self._mods or self._buf_exists(9)

    @property
    def owner_name__type(self):
        return ProtoBase.TYPE_string

    def _finalize_owner_name(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(9)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(9)

    _pbf_finalizers.append(_finalize_owner_name)


    def _get_is_egg(self):
        if 10 in self._cache:
            r = self._cache[10]
        else:
            r = self._buf_get(10, ProtoBase.TYPE_bool, 'is_egg')
            self._cache[10] = r
        return r

    def _establish_parentage_is_egg(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_is_egg), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_is_egg
                v._pbf_establish_parent_callback = self._establish_parentage_is_egg

    def _set_is_egg(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_is_egg(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field is_egg"
            raise ProtoValueError(list_assign_error)
        self._cache[10] = v
        self._mods[10] = ProtoBase.TYPE_bool

    def _mod_is_egg(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[10] = ProtoBase.TYPE_bool

    def _del_is_egg(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 10 in self._cache:
            del self._cache[10]
        if 10 in self._mods:
            del self._mods[10]
        self._buf_del(10)

    _pb_field_name_10 = "is_egg"

    is_egg = property(_get_is_egg, _set_is_egg, _del_is_egg)

    @property
    def is_egg__exists(self):
        return 10 in self._mods or self._buf_exists(10)

    @property
    def is_egg__type(self):
        return ProtoBase.TYPE_bool

    def _finalize_is_egg(cls):
        if is_string(ProtoBase.TYPE_bool):
            cls._pbf_strings.append(10)
        elif _PB_type(ProtoBase.TYPE_bool) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bool, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bool.pb_subtype):
                cls._pbf_strings.append(10)

    _pbf_finalizers.append(_finalize_is_egg)


    def _get_egg_km_walked_target(self):
        if 11 in self._cache:
            r = self._cache[11]
        else:
            r = self._buf_get(11, ProtoBase.TYPE_int32, 'egg_km_walked_target')
            self._cache[11] = r
        return r

    def _establish_parentage_egg_km_walked_target(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_egg_km_walked_target), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_egg_km_walked_target
                v._pbf_establish_parent_callback = self._establish_parentage_egg_km_walked_target

    def _set_egg_km_walked_target(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_egg_km_walked_target(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field egg_km_walked_target"
            raise ProtoValueError(list_assign_error)
        self._cache[11] = v
        self._mods[11] = ProtoBase.TYPE_int32

    def _mod_egg_km_walked_target(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[11] = ProtoBase.TYPE_int32

    def _del_egg_km_walked_target(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 11 in self._cache:
            del self._cache[11]
        if 11 in self._mods:
            del self._mods[11]
        self._buf_del(11)

    _pb_field_name_11 = "egg_km_walked_target"

    egg_km_walked_target = property(_get_egg_km_walked_target, _set_egg_km_walked_target, _del_egg_km_walked_target)

    @property
    def egg_km_walked_target__exists(self):
        return 11 in self._mods or self._buf_exists(11)

    @property
    def egg_km_walked_target__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_egg_km_walked_target(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(11)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(11)

    _pbf_finalizers.append(_finalize_egg_km_walked_target)


    def _get_egg_km_walked_start(self):
        if 12 in self._cache:
            r = self._cache[12]
        else:
            r = self._buf_get(12, ProtoBase.TYPE_int32, 'egg_km_walked_start')
            self._cache[12] = r
        return r

    def _establish_parentage_egg_km_walked_start(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_egg_km_walked_start), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_egg_km_walked_start
                v._pbf_establish_parent_callback = self._establish_parentage_egg_km_walked_start

    def _set_egg_km_walked_start(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_egg_km_walked_start(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field egg_km_walked_start"
            raise ProtoValueError(list_assign_error)
        self._cache[12] = v
        self._mods[12] = ProtoBase.TYPE_int32

    def _mod_egg_km_walked_start(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[12] = ProtoBase.TYPE_int32

    def _del_egg_km_walked_start(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 12 in self._cache:
            del self._cache[12]
        if 12 in self._mods:
            del self._mods[12]
        self._buf_del(12)

    _pb_field_name_12 = "egg_km_walked_start"

    egg_km_walked_start = property(_get_egg_km_walked_start, _set_egg_km_walked_start, _del_egg_km_walked_start)

    @property
    def egg_km_walked_start__exists(self):
        return 12 in self._mods or self._buf_exists(12)

    @property
    def egg_km_walked_start__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_egg_km_walked_start(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(12)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(12)

    _pbf_finalizers.append(_finalize_egg_km_walked_start)


    def _get_origin(self):
        if 14 in self._cache:
            r = self._cache[14]
        else:
            r = self._buf_get(14, ProtoBase.TYPE_int32, 'origin')
            self._cache[14] = r
        return r

    def _establish_parentage_origin(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_origin), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_origin
                v._pbf_establish_parent_callback = self._establish_parentage_origin

    def _set_origin(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_origin(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field origin"
            raise ProtoValueError(list_assign_error)
        self._cache[14] = v
        self._mods[14] = ProtoBase.TYPE_int32

    def _mod_origin(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[14] = ProtoBase.TYPE_int32

    def _del_origin(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 14 in self._cache:
            del self._cache[14]
        if 14 in self._mods:
            del self._mods[14]
        self._buf_del(14)

    _pb_field_name_14 = "origin"

    origin = property(_get_origin, _set_origin, _del_origin)

    @property
    def origin__exists(self):
        return 14 in self._mods or self._buf_exists(14)

    @property
    def origin__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_origin(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(14)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(14)

    _pbf_finalizers.append(_finalize_origin)


    def _get_height_m(self):
        if 15 in self._cache:
            r = self._cache[15]
        else:
            r = self._buf_get(15, ProtoBase.TYPE_float, 'height_m')
            self._cache[15] = r
        return r

    def _establish_parentage_height_m(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_height_m), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_height_m
                v._pbf_establish_parent_callback = self._establish_parentage_height_m

    def _set_height_m(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_height_m(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field height_m"
            raise ProtoValueError(list_assign_error)
        self._cache[15] = v
        self._mods[15] = ProtoBase.TYPE_float

    def _mod_height_m(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[15] = ProtoBase.TYPE_float

    def _del_height_m(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 15 in self._cache:
            del self._cache[15]
        if 15 in self._mods:
            del self._mods[15]
        self._buf_del(15)

    _pb_field_name_15 = "height_m"

    height_m = property(_get_height_m, _set_height_m, _del_height_m)

    @property
    def height_m__exists(self):
        return 15 in self._mods or self._buf_exists(15)

    @property
    def height_m__type(self):
        return ProtoBase.TYPE_float

    def _finalize_height_m(cls):
        if is_string(ProtoBase.TYPE_float):
            cls._pbf_strings.append(15)
        elif _PB_type(ProtoBase.TYPE_float) is _PB_type:
            assert issubclass(ProtoBase.TYPE_float, RepeatedSequence)
            if is_string(ProtoBase.TYPE_float.pb_subtype):
                cls._pbf_strings.append(15)

    _pbf_finalizers.append(_finalize_height_m)


    def _get_weight_kg(self):
        if 16 in self._cache:
            r = self._cache[16]
        else:
            r = self._buf_get(16, ProtoBase.TYPE_float, 'weight_kg')
            self._cache[16] = r
        return r

    def _establish_parentage_weight_kg(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_weight_kg), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_weight_kg
                v._pbf_establish_parent_callback = self._establish_parentage_weight_kg

    def _set_weight_kg(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_weight_kg(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field weight_kg"
            raise ProtoValueError(list_assign_error)
        self._cache[16] = v
        self._mods[16] = ProtoBase.TYPE_float

    def _mod_weight_kg(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[16] = ProtoBase.TYPE_float

    def _del_weight_kg(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 16 in self._cache:
            del self._cache[16]
        if 16 in self._mods:
            del self._mods[16]
        self._buf_del(16)

    _pb_field_name_16 = "weight_kg"

    weight_kg = property(_get_weight_kg, _set_weight_kg, _del_weight_kg)

    @property
    def weight_kg__exists(self):
        return 16 in self._mods or self._buf_exists(16)

    @property
    def weight_kg__type(self):
        return ProtoBase.TYPE_float

    def _finalize_weight_kg(cls):
        if is_string(ProtoBase.TYPE_float):
            cls._pbf_strings.append(16)
        elif _PB_type(ProtoBase.TYPE_float) is _PB_type:
            assert issubclass(ProtoBase.TYPE_float, RepeatedSequence)
            if is_string(ProtoBase.TYPE_float.pb_subtype):
                cls._pbf_strings.append(16)

    _pbf_finalizers.append(_finalize_weight_kg)


    def _get_individual_attack(self):
        if 17 in self._cache:
            r = self._cache[17]
        else:
            r = self._buf_get(17, ProtoBase.TYPE_int32, 'individual_attack')
            self._cache[17] = r
        return r

    def _establish_parentage_individual_attack(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_individual_attack), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_individual_attack
                v._pbf_establish_parent_callback = self._establish_parentage_individual_attack

    def _set_individual_attack(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_individual_attack(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field individual_attack"
            raise ProtoValueError(list_assign_error)
        self._cache[17] = v
        self._mods[17] = ProtoBase.TYPE_int32

    def _mod_individual_attack(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[17] = ProtoBase.TYPE_int32

    def _del_individual_attack(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 17 in self._cache:
            del self._cache[17]
        if 17 in self._mods:
            del self._mods[17]
        self._buf_del(17)

    _pb_field_name_17 = "individual_attack"

    individual_attack = property(_get_individual_attack, _set_individual_attack, _del_individual_attack)

    @property
    def individual_attack__exists(self):
        return 17 in self._mods or self._buf_exists(17)

    @property
    def individual_attack__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_individual_attack(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(17)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(17)

    _pbf_finalizers.append(_finalize_individual_attack)


    def _get_individual_defense(self):
        if 18 in self._cache:
            r = self._cache[18]
        else:
            r = self._buf_get(18, ProtoBase.TYPE_int32, 'individual_defense')
            self._cache[18] = r
        return r

    def _establish_parentage_individual_defense(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_individual_defense), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_individual_defense
                v._pbf_establish_parent_callback = self._establish_parentage_individual_defense

    def _set_individual_defense(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_individual_defense(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field individual_defense"
            raise ProtoValueError(list_assign_error)
        self._cache[18] = v
        self._mods[18] = ProtoBase.TYPE_int32

    def _mod_individual_defense(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[18] = ProtoBase.TYPE_int32

    def _del_individual_defense(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 18 in self._cache:
            del self._cache[18]
        if 18 in self._mods:
            del self._mods[18]
        self._buf_del(18)

    _pb_field_name_18 = "individual_defense"

    individual_defense = property(_get_individual_defense, _set_individual_defense, _del_individual_defense)

    @property
    def individual_defense__exists(self):
        return 18 in self._mods or self._buf_exists(18)

    @property
    def individual_defense__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_individual_defense(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(18)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(18)

    _pbf_finalizers.append(_finalize_individual_defense)


    def _get_individual_stamina(self):
        if 19 in self._cache:
            r = self._cache[19]
        else:
            r = self._buf_get(19, ProtoBase.TYPE_int32, 'individual_stamina')
            self._cache[19] = r
        return r

    def _establish_parentage_individual_stamina(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_individual_stamina), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_individual_stamina
                v._pbf_establish_parent_callback = self._establish_parentage_individual_stamina

    def _set_individual_stamina(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_individual_stamina(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field individual_stamina"
            raise ProtoValueError(list_assign_error)
        self._cache[19] = v
        self._mods[19] = ProtoBase.TYPE_int32

    def _mod_individual_stamina(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[19] = ProtoBase.TYPE_int32

    def _del_individual_stamina(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 19 in self._cache:
            del self._cache[19]
        if 19 in self._mods:
            del self._mods[19]
        self._buf_del(19)

    _pb_field_name_19 = "individual_stamina"

    individual_stamina = property(_get_individual_stamina, _set_individual_stamina, _del_individual_stamina)

    @property
    def individual_stamina__exists(self):
        return 19 in self._mods or self._buf_exists(19)

    @property
    def individual_stamina__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_individual_stamina(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(19)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(19)

    _pbf_finalizers.append(_finalize_individual_stamina)


    def _get_cp_multiplier(self):
        if 20 in self._cache:
            r = self._cache[20]
        else:
            r = self._buf_get(20, ProtoBase.TYPE_int32, 'cp_multiplier')
            self._cache[20] = r
        return r

    def _establish_parentage_cp_multiplier(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_cp_multiplier), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_cp_multiplier
                v._pbf_establish_parent_callback = self._establish_parentage_cp_multiplier

    def _set_cp_multiplier(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_cp_multiplier(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field cp_multiplier"
            raise ProtoValueError(list_assign_error)
        self._cache[20] = v
        self._mods[20] = ProtoBase.TYPE_int32

    def _mod_cp_multiplier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[20] = ProtoBase.TYPE_int32

    def _del_cp_multiplier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 20 in self._cache:
            del self._cache[20]
        if 20 in self._mods:
            del self._mods[20]
        self._buf_del(20)

    _pb_field_name_20 = "cp_multiplier"

    cp_multiplier = property(_get_cp_multiplier, _set_cp_multiplier, _del_cp_multiplier)

    @property
    def cp_multiplier__exists(self):
        return 20 in self._mods or self._buf_exists(20)

    @property
    def cp_multiplier__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_cp_multiplier(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(20)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(20)

    _pbf_finalizers.append(_finalize_cp_multiplier)


    def _get_pokeball(self):
        if 21 in self._cache:
            r = self._cache[21]
        else:
            r = self._buf_get(21, ProtoBase.TYPE_int32, 'pokeball')
            self._cache[21] = r
        return r

    def _establish_parentage_pokeball(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokeball), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokeball
                v._pbf_establish_parent_callback = self._establish_parentage_pokeball

    def _set_pokeball(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokeball(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokeball"
            raise ProtoValueError(list_assign_error)
        self._cache[21] = v
        self._mods[21] = ProtoBase.TYPE_int32

    def _mod_pokeball(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[21] = ProtoBase.TYPE_int32

    def _del_pokeball(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 21 in self._cache:
            del self._cache[21]
        if 21 in self._mods:
            del self._mods[21]
        self._buf_del(21)

    _pb_field_name_21 = "pokeball"

    pokeball = property(_get_pokeball, _set_pokeball, _del_pokeball)

    @property
    def pokeball__exists(self):
        return 21 in self._mods or self._buf_exists(21)

    @property
    def pokeball__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_pokeball(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(21)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(21)

    _pbf_finalizers.append(_finalize_pokeball)


    def _get_captured_cell_id(self):
        if 22 in self._cache:
            r = self._cache[22]
        else:
            r = self._buf_get(22, ProtoBase.TYPE_uint64, 'captured_cell_id')
            self._cache[22] = r
        return r

    def _establish_parentage_captured_cell_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_captured_cell_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_captured_cell_id
                v._pbf_establish_parent_callback = self._establish_parentage_captured_cell_id

    def _set_captured_cell_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_captured_cell_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field captured_cell_id"
            raise ProtoValueError(list_assign_error)
        self._cache[22] = v
        self._mods[22] = ProtoBase.TYPE_uint64

    def _mod_captured_cell_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[22] = ProtoBase.TYPE_uint64

    def _del_captured_cell_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 22 in self._cache:
            del self._cache[22]
        if 22 in self._mods:
            del self._mods[22]
        self._buf_del(22)

    _pb_field_name_22 = "captured_cell_id"

    captured_cell_id = property(_get_captured_cell_id, _set_captured_cell_id, _del_captured_cell_id)

    @property
    def captured_cell_id__exists(self):
        return 22 in self._mods or self._buf_exists(22)

    @property
    def captured_cell_id__type(self):
        return ProtoBase.TYPE_uint64

    def _finalize_captured_cell_id(cls):
        if is_string(ProtoBase.TYPE_uint64):
            cls._pbf_strings.append(22)
        elif _PB_type(ProtoBase.TYPE_uint64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_uint64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_uint64.pb_subtype):
                cls._pbf_strings.append(22)

    _pbf_finalizers.append(_finalize_captured_cell_id)


    def _get_battles_attacked(self):
        if 23 in self._cache:
            r = self._cache[23]
        else:
            r = self._buf_get(23, ProtoBase.TYPE_int32, 'battles_attacked')
            self._cache[23] = r
        return r

    def _establish_parentage_battles_attacked(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_battles_attacked), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_battles_attacked
                v._pbf_establish_parent_callback = self._establish_parentage_battles_attacked

    def _set_battles_attacked(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_battles_attacked(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field battles_attacked"
            raise ProtoValueError(list_assign_error)
        self._cache[23] = v
        self._mods[23] = ProtoBase.TYPE_int32

    def _mod_battles_attacked(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[23] = ProtoBase.TYPE_int32

    def _del_battles_attacked(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 23 in self._cache:
            del self._cache[23]
        if 23 in self._mods:
            del self._mods[23]
        self._buf_del(23)

    _pb_field_name_23 = "battles_attacked"

    battles_attacked = property(_get_battles_attacked, _set_battles_attacked, _del_battles_attacked)

    @property
    def battles_attacked__exists(self):
        return 23 in self._mods or self._buf_exists(23)

    @property
    def battles_attacked__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_battles_attacked(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(23)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(23)

    _pbf_finalizers.append(_finalize_battles_attacked)


    def _get_battles_defended(self):
        if 24 in self._cache:
            r = self._cache[24]
        else:
            r = self._buf_get(24, ProtoBase.TYPE_int32, 'battles_defended')
            self._cache[24] = r
        return r

    def _establish_parentage_battles_defended(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_battles_defended), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_battles_defended
                v._pbf_establish_parent_callback = self._establish_parentage_battles_defended

    def _set_battles_defended(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_battles_defended(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field battles_defended"
            raise ProtoValueError(list_assign_error)
        self._cache[24] = v
        self._mods[24] = ProtoBase.TYPE_int32

    def _mod_battles_defended(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[24] = ProtoBase.TYPE_int32

    def _del_battles_defended(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 24 in self._cache:
            del self._cache[24]
        if 24 in self._mods:
            del self._mods[24]
        self._buf_del(24)

    _pb_field_name_24 = "battles_defended"

    battles_defended = property(_get_battles_defended, _set_battles_defended, _del_battles_defended)

    @property
    def battles_defended__exists(self):
        return 24 in self._mods or self._buf_exists(24)

    @property
    def battles_defended__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_battles_defended(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(24)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(24)

    _pbf_finalizers.append(_finalize_battles_defended)


    def _get_egg_incubator_id(self):
        if 25 in self._cache:
            r = self._cache[25]
        else:
            r = self._buf_get(25, ProtoBase.TYPE_int32, 'egg_incubator_id')
            self._cache[25] = r
        return r

    def _establish_parentage_egg_incubator_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_egg_incubator_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_egg_incubator_id
                v._pbf_establish_parent_callback = self._establish_parentage_egg_incubator_id

    def _set_egg_incubator_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_egg_incubator_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field egg_incubator_id"
            raise ProtoValueError(list_assign_error)
        self._cache[25] = v
        self._mods[25] = ProtoBase.TYPE_int32

    def _mod_egg_incubator_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[25] = ProtoBase.TYPE_int32

    def _del_egg_incubator_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 25 in self._cache:
            del self._cache[25]
        if 25 in self._mods:
            del self._mods[25]
        self._buf_del(25)

    _pb_field_name_25 = "egg_incubator_id"

    egg_incubator_id = property(_get_egg_incubator_id, _set_egg_incubator_id, _del_egg_incubator_id)

    @property
    def egg_incubator_id__exists(self):
        return 25 in self._mods or self._buf_exists(25)

    @property
    def egg_incubator_id__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_egg_incubator_id(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(25)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(25)

    _pbf_finalizers.append(_finalize_egg_incubator_id)


    def _get_creation_time_ms(self):
        if 26 in self._cache:
            r = self._cache[26]
        else:
            r = self._buf_get(26, ProtoBase.TYPE_uint64, 'creation_time_ms')
            self._cache[26] = r
        return r

    def _establish_parentage_creation_time_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_creation_time_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_creation_time_ms
                v._pbf_establish_parent_callback = self._establish_parentage_creation_time_ms

    def _set_creation_time_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_creation_time_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field creation_time_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[26] = v
        self._mods[26] = ProtoBase.TYPE_uint64

    def _mod_creation_time_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[26] = ProtoBase.TYPE_uint64

    def _del_creation_time_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 26 in self._cache:
            del self._cache[26]
        if 26 in self._mods:
            del self._mods[26]
        self._buf_del(26)

    _pb_field_name_26 = "creation_time_ms"

    creation_time_ms = property(_get_creation_time_ms, _set_creation_time_ms, _del_creation_time_ms)

    @property
    def creation_time_ms__exists(self):
        return 26 in self._mods or self._buf_exists(26)

    @property
    def creation_time_ms__type(self):
        return ProtoBase.TYPE_uint64

    def _finalize_creation_time_ms(cls):
        if is_string(ProtoBase.TYPE_uint64):
            cls._pbf_strings.append(26)
        elif _PB_type(ProtoBase.TYPE_uint64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_uint64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_uint64.pb_subtype):
                cls._pbf_strings.append(26)

    _pbf_finalizers.append(_finalize_creation_time_ms)


    def _get_num_upgrades(self):
        if 27 in self._cache:
            r = self._cache[27]
        else:
            r = self._buf_get(27, ProtoBase.TYPE_int32, 'num_upgrades')
            self._cache[27] = r
        return r

    def _establish_parentage_num_upgrades(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_num_upgrades), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_num_upgrades
                v._pbf_establish_parent_callback = self._establish_parentage_num_upgrades

    def _set_num_upgrades(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_num_upgrades(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field num_upgrades"
            raise ProtoValueError(list_assign_error)
        self._cache[27] = v
        self._mods[27] = ProtoBase.TYPE_int32

    def _mod_num_upgrades(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[27] = ProtoBase.TYPE_int32

    def _del_num_upgrades(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 27 in self._cache:
            del self._cache[27]
        if 27 in self._mods:
            del self._mods[27]
        self._buf_del(27)

    _pb_field_name_27 = "num_upgrades"

    num_upgrades = property(_get_num_upgrades, _set_num_upgrades, _del_num_upgrades)

    @property
    def num_upgrades__exists(self):
        return 27 in self._mods or self._buf_exists(27)

    @property
    def num_upgrades__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_num_upgrades(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(27)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(27)

    _pbf_finalizers.append(_finalize_num_upgrades)


    def _get_additional_cp_multiplier(self):
        if 28 in self._cache:
            r = self._cache[28]
        else:
            r = self._buf_get(28, ProtoBase.TYPE_int32, 'additional_cp_multiplier')
            self._cache[28] = r
        return r

    def _establish_parentage_additional_cp_multiplier(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_additional_cp_multiplier), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_additional_cp_multiplier
                v._pbf_establish_parent_callback = self._establish_parentage_additional_cp_multiplier

    def _set_additional_cp_multiplier(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_additional_cp_multiplier(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field additional_cp_multiplier"
            raise ProtoValueError(list_assign_error)
        self._cache[28] = v
        self._mods[28] = ProtoBase.TYPE_int32

    def _mod_additional_cp_multiplier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[28] = ProtoBase.TYPE_int32

    def _del_additional_cp_multiplier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 28 in self._cache:
            del self._cache[28]
        if 28 in self._mods:
            del self._mods[28]
        self._buf_del(28)

    _pb_field_name_28 = "additional_cp_multiplier"

    additional_cp_multiplier = property(_get_additional_cp_multiplier, _set_additional_cp_multiplier, _del_additional_cp_multiplier)

    @property
    def additional_cp_multiplier__exists(self):
        return 28 in self._mods or self._buf_exists(28)

    @property
    def additional_cp_multiplier__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_additional_cp_multiplier(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(28)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(28)

    _pbf_finalizers.append(_finalize_additional_cp_multiplier)


    def _get_favorite(self):
        if 29 in self._cache:
            r = self._cache[29]
        else:
            r = self._buf_get(29, ProtoBase.TYPE_int32, 'favorite')
            self._cache[29] = r
        return r

    def _establish_parentage_favorite(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_favorite), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_favorite
                v._pbf_establish_parent_callback = self._establish_parentage_favorite

    def _set_favorite(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_favorite(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field favorite"
            raise ProtoValueError(list_assign_error)
        self._cache[29] = v
        self._mods[29] = ProtoBase.TYPE_int32

    def _mod_favorite(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[29] = ProtoBase.TYPE_int32

    def _del_favorite(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 29 in self._cache:
            del self._cache[29]
        if 29 in self._mods:
            del self._mods[29]
        self._buf_del(29)

    _pb_field_name_29 = "favorite"

    favorite = property(_get_favorite, _set_favorite, _del_favorite)

    @property
    def favorite__exists(self):
        return 29 in self._mods or self._buf_exists(29)

    @property
    def favorite__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_favorite(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(29)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(29)

    _pbf_finalizers.append(_finalize_favorite)


    def _get_nickname(self):
        if 30 in self._cache:
            r = self._cache[30]
        else:
            r = self._buf_get(30, ProtoBase.TYPE_string, 'nickname')
            self._cache[30] = r
        return r

    def _establish_parentage_nickname(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_nickname), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_nickname
                v._pbf_establish_parent_callback = self._establish_parentage_nickname

    def _set_nickname(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_nickname(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field nickname"
            raise ProtoValueError(list_assign_error)
        self._cache[30] = v
        self._mods[30] = ProtoBase.TYPE_string

    def _mod_nickname(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[30] = ProtoBase.TYPE_string

    def _del_nickname(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 30 in self._cache:
            del self._cache[30]
        if 30 in self._mods:
            del self._mods[30]
        self._buf_del(30)

    _pb_field_name_30 = "nickname"

    nickname = property(_get_nickname, _set_nickname, _del_nickname)

    @property
    def nickname__exists(self):
        return 30 in self._mods or self._buf_exists(30)

    @property
    def nickname__type(self):
        return ProtoBase.TYPE_string

    def _finalize_nickname(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(30)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(30)

    _pbf_finalizers.append(_finalize_nickname)


    def _get_from_fort(self):
        if 31 in self._cache:
            r = self._cache[31]
        else:
            r = self._buf_get(31, ProtoBase.TYPE_int32, 'from_fort')
            self._cache[31] = r
        return r

    def _establish_parentage_from_fort(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_from_fort), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_from_fort
                v._pbf_establish_parent_callback = self._establish_parentage_from_fort

    def _set_from_fort(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_from_fort(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field from_fort"
            raise ProtoValueError(list_assign_error)
        self._cache[31] = v
        self._mods[31] = ProtoBase.TYPE_int32

    def _mod_from_fort(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[31] = ProtoBase.TYPE_int32

    def _del_from_fort(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 31 in self._cache:
            del self._cache[31]
        if 31 in self._mods:
            del self._mods[31]
        self._buf_del(31)

    _pb_field_name_31 = "from_fort"

    from_fort = property(_get_from_fort, _set_from_fort, _del_from_fort)

    @property
    def from_fort__exists(self):
        return 31 in self._mods or self._buf_exists(31)

    @property
    def from_fort__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_from_fort(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(31)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(31)

    _pbf_finalizers.append(_finalize_from_fort)


TYPE_Pokemon = Pokemon
_PB_finalizers.append('Pokemon')

class Item(ProtoBase):
    _required = []
    _field_map = {'count': 2, 'item': 1, 'unseen': 3}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['item', 'count', 'unseen']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_item(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, RpcEnum_palm.TYPE_ItemType, 'item')
            self._cache[1] = r
        return r

    def _establish_parentage_item(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_item), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_item
                v._pbf_establish_parent_callback = self._establish_parentage_item

    def _set_item(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_item(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field item"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = RpcEnum_palm.TYPE_ItemType

    def _mod_item(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = RpcEnum_palm.TYPE_ItemType

    def _del_item(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "item"

    item = property(_get_item, _set_item, _del_item)

    @property
    def item__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def item__type(self):
        return RpcEnum_palm.TYPE_ItemType

    def _finalize_item(cls):
        if is_string(RpcEnum_palm.TYPE_ItemType):
            cls._pbf_strings.append(1)
        elif _PB_type(RpcEnum_palm.TYPE_ItemType) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_ItemType, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_ItemType.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_item)


    def _get_count(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int32, 'count')
            self._cache[2] = r
        return r

    def _establish_parentage_count(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_count), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_count
                v._pbf_establish_parent_callback = self._establish_parentage_count

    def _set_count(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_count(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field count"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_int32

    def _mod_count(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int32

    def _del_count(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "count"

    count = property(_get_count, _set_count, _del_count)

    @property
    def count__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def count__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_count(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_count)


    def _get_unseen(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_bool, 'unseen')
            self._cache[3] = r
        return r

    def _establish_parentage_unseen(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_unseen), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_unseen
                v._pbf_establish_parent_callback = self._establish_parentage_unseen

    def _set_unseen(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_unseen(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field unseen"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_bool

    def _mod_unseen(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_bool

    def _del_unseen(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "unseen"

    unseen = property(_get_unseen, _set_unseen, _del_unseen)

    @property
    def unseen__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def unseen__type(self):
        return ProtoBase.TYPE_bool

    def _finalize_unseen(cls):
        if is_string(ProtoBase.TYPE_bool):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_bool) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bool, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bool.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_unseen)


TYPE_Item = Item
_PB_finalizers.append('Item')

class PokedexEntry(ProtoBase):
    _required = []
    _field_map = {'times_captured': 3, 'times_encountered': 2, 'evolution_stones': 5, 'pokedex_entry_number': 1, 'evolution_stone_pieces': 4}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['pokedex_entry_number', 'times_encountered', 'times_captured', 'evolution_stone_pieces', 'evolution_stones']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_pokedex_entry_number(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_int32, 'pokedex_entry_number')
            self._cache[1] = r
        return r

    def _establish_parentage_pokedex_entry_number(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokedex_entry_number), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokedex_entry_number
                v._pbf_establish_parent_callback = self._establish_parentage_pokedex_entry_number

    def _set_pokedex_entry_number(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokedex_entry_number(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokedex_entry_number"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_int32

    def _mod_pokedex_entry_number(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_int32

    def _del_pokedex_entry_number(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "pokedex_entry_number"

    pokedex_entry_number = property(_get_pokedex_entry_number, _set_pokedex_entry_number, _del_pokedex_entry_number)

    @property
    def pokedex_entry_number__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def pokedex_entry_number__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_pokedex_entry_number(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_pokedex_entry_number)


    def _get_times_encountered(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int32, 'times_encountered')
            self._cache[2] = r
        return r

    def _establish_parentage_times_encountered(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_times_encountered), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_times_encountered
                v._pbf_establish_parent_callback = self._establish_parentage_times_encountered

    def _set_times_encountered(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_times_encountered(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field times_encountered"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_int32

    def _mod_times_encountered(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int32

    def _del_times_encountered(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "times_encountered"

    times_encountered = property(_get_times_encountered, _set_times_encountered, _del_times_encountered)

    @property
    def times_encountered__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def times_encountered__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_times_encountered(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_times_encountered)


    def _get_times_captured(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_int32, 'times_captured')
            self._cache[3] = r
        return r

    def _establish_parentage_times_captured(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_times_captured), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_times_captured
                v._pbf_establish_parent_callback = self._establish_parentage_times_captured

    def _set_times_captured(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_times_captured(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field times_captured"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_int32

    def _mod_times_captured(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_int32

    def _del_times_captured(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "times_captured"

    times_captured = property(_get_times_captured, _set_times_captured, _del_times_captured)

    @property
    def times_captured__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def times_captured__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_times_captured(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_times_captured)


    def _get_evolution_stone_pieces(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, ProtoBase.TYPE_int32, 'evolution_stone_pieces')
            self._cache[4] = r
        return r

    def _establish_parentage_evolution_stone_pieces(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_evolution_stone_pieces), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_evolution_stone_pieces
                v._pbf_establish_parent_callback = self._establish_parentage_evolution_stone_pieces

    def _set_evolution_stone_pieces(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_evolution_stone_pieces(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field evolution_stone_pieces"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = ProtoBase.TYPE_int32

    def _mod_evolution_stone_pieces(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = ProtoBase.TYPE_int32

    def _del_evolution_stone_pieces(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "evolution_stone_pieces"

    evolution_stone_pieces = property(_get_evolution_stone_pieces, _set_evolution_stone_pieces, _del_evolution_stone_pieces)

    @property
    def evolution_stone_pieces__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def evolution_stone_pieces__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_evolution_stone_pieces(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(4)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_evolution_stone_pieces)


    def _get_evolution_stones(self):
        if 5 in self._cache:
            r = self._cache[5]
        else:
            r = self._buf_get(5, ProtoBase.TYPE_int32, 'evolution_stones')
            self._cache[5] = r
        return r

    def _establish_parentage_evolution_stones(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_evolution_stones), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_evolution_stones
                v._pbf_establish_parent_callback = self._establish_parentage_evolution_stones

    def _set_evolution_stones(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_evolution_stones(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field evolution_stones"
            raise ProtoValueError(list_assign_error)
        self._cache[5] = v
        self._mods[5] = ProtoBase.TYPE_int32

    def _mod_evolution_stones(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[5] = ProtoBase.TYPE_int32

    def _del_evolution_stones(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 5 in self._cache:
            del self._cache[5]
        if 5 in self._mods:
            del self._mods[5]
        self._buf_del(5)

    _pb_field_name_5 = "evolution_stones"

    evolution_stones = property(_get_evolution_stones, _set_evolution_stones, _del_evolution_stones)

    @property
    def evolution_stones__exists(self):
        return 5 in self._mods or self._buf_exists(5)

    @property
    def evolution_stones__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_evolution_stones(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(5)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(5)

    _pbf_finalizers.append(_finalize_evolution_stones)


TYPE_PokedexEntry = PokedexEntry
_PB_finalizers.append('PokedexEntry')

class PlayerStats(ProtoBase):
    _required = []
    _field_map = {'big_magikarp_caught': 13, 'pokemons_encountered': 6, 'pokemon_deployed': 21, 'small_rattata_caught': 23, 'battle_attack_total': 15, 'next_level_xp': 4, 'pokemons_captured': 8, 'battle_attack_won': 14, 'prestige_raised_total': 19, 'pokemon_caught_by_type': 22, 'pokeballs_thrown': 11, 'evolutions': 9, 'eggs_hatched': 12, 'prestige_dropped_total': 20, 'prev_level_xp': 3, 'battle_training_total': 18, 'unique_pokedex_entries': 7, 'km_walked': 5, 'level': 1, 'experience': 2, 'poke_stop_visits': 10, 'battle_defended_won': 16, 'battle_training_won': 17}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['level', 'experience', 'prev_level_xp', 'next_level_xp', 'km_walked', 'pokemons_encountered', 'unique_pokedex_entries', 'pokemons_captured', 'evolutions', 'poke_stop_visits', 'pokeballs_thrown', 'eggs_hatched', 'big_magikarp_caught', 'battle_attack_won', 'battle_attack_total', 'battle_defended_won', 'battle_training_won', 'battle_training_total', 'prestige_raised_total', 'prestige_dropped_total', 'pokemon_deployed', 'pokemon_caught_by_type', 'small_rattata_caught']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_level(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_int32, 'level')
            self._cache[1] = r
        return r

    def _establish_parentage_level(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_level), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_level
                v._pbf_establish_parent_callback = self._establish_parentage_level

    def _set_level(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_level(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field level"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_int32

    def _mod_level(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_int32

    def _del_level(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "level"

    level = property(_get_level, _set_level, _del_level)

    @property
    def level__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def level__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_level(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_level)


    def _get_experience(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int64, 'experience')
            self._cache[2] = r
        return r

    def _establish_parentage_experience(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_experience), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_experience
                v._pbf_establish_parent_callback = self._establish_parentage_experience

    def _set_experience(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_experience(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field experience"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_int64

    def _mod_experience(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int64

    def _del_experience(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "experience"

    experience = property(_get_experience, _set_experience, _del_experience)

    @property
    def experience__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def experience__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_experience(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_experience)


    def _get_prev_level_xp(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_int64, 'prev_level_xp')
            self._cache[3] = r
        return r

    def _establish_parentage_prev_level_xp(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_prev_level_xp), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_prev_level_xp
                v._pbf_establish_parent_callback = self._establish_parentage_prev_level_xp

    def _set_prev_level_xp(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_prev_level_xp(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field prev_level_xp"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_int64

    def _mod_prev_level_xp(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_int64

    def _del_prev_level_xp(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "prev_level_xp"

    prev_level_xp = property(_get_prev_level_xp, _set_prev_level_xp, _del_prev_level_xp)

    @property
    def prev_level_xp__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def prev_level_xp__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_prev_level_xp(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_prev_level_xp)


    def _get_next_level_xp(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, ProtoBase.TYPE_int64, 'next_level_xp')
            self._cache[4] = r
        return r

    def _establish_parentage_next_level_xp(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_next_level_xp), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_next_level_xp
                v._pbf_establish_parent_callback = self._establish_parentage_next_level_xp

    def _set_next_level_xp(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_next_level_xp(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field next_level_xp"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = ProtoBase.TYPE_int64

    def _mod_next_level_xp(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = ProtoBase.TYPE_int64

    def _del_next_level_xp(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "next_level_xp"

    next_level_xp = property(_get_next_level_xp, _set_next_level_xp, _del_next_level_xp)

    @property
    def next_level_xp__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def next_level_xp__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_next_level_xp(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(4)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_next_level_xp)


    def _get_km_walked(self):
        if 5 in self._cache:
            r = self._cache[5]
        else:
            r = self._buf_get(5, ProtoBase.TYPE_float, 'km_walked')
            self._cache[5] = r
        return r

    def _establish_parentage_km_walked(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_km_walked), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_km_walked
                v._pbf_establish_parent_callback = self._establish_parentage_km_walked

    def _set_km_walked(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_km_walked(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field km_walked"
            raise ProtoValueError(list_assign_error)
        self._cache[5] = v
        self._mods[5] = ProtoBase.TYPE_float

    def _mod_km_walked(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[5] = ProtoBase.TYPE_float

    def _del_km_walked(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 5 in self._cache:
            del self._cache[5]
        if 5 in self._mods:
            del self._mods[5]
        self._buf_del(5)

    _pb_field_name_5 = "km_walked"

    km_walked = property(_get_km_walked, _set_km_walked, _del_km_walked)

    @property
    def km_walked__exists(self):
        return 5 in self._mods or self._buf_exists(5)

    @property
    def km_walked__type(self):
        return ProtoBase.TYPE_float

    def _finalize_km_walked(cls):
        if is_string(ProtoBase.TYPE_float):
            cls._pbf_strings.append(5)
        elif _PB_type(ProtoBase.TYPE_float) is _PB_type:
            assert issubclass(ProtoBase.TYPE_float, RepeatedSequence)
            if is_string(ProtoBase.TYPE_float.pb_subtype):
                cls._pbf_strings.append(5)

    _pbf_finalizers.append(_finalize_km_walked)


    def _get_pokemons_encountered(self):
        if 6 in self._cache:
            r = self._cache[6]
        else:
            r = self._buf_get(6, ProtoBase.TYPE_int32, 'pokemons_encountered')
            self._cache[6] = r
        return r

    def _establish_parentage_pokemons_encountered(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokemons_encountered), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokemons_encountered
                v._pbf_establish_parent_callback = self._establish_parentage_pokemons_encountered

    def _set_pokemons_encountered(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokemons_encountered(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokemons_encountered"
            raise ProtoValueError(list_assign_error)
        self._cache[6] = v
        self._mods[6] = ProtoBase.TYPE_int32

    def _mod_pokemons_encountered(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[6] = ProtoBase.TYPE_int32

    def _del_pokemons_encountered(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 6 in self._cache:
            del self._cache[6]
        if 6 in self._mods:
            del self._mods[6]
        self._buf_del(6)

    _pb_field_name_6 = "pokemons_encountered"

    pokemons_encountered = property(_get_pokemons_encountered, _set_pokemons_encountered, _del_pokemons_encountered)

    @property
    def pokemons_encountered__exists(self):
        return 6 in self._mods or self._buf_exists(6)

    @property
    def pokemons_encountered__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_pokemons_encountered(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(6)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(6)

    _pbf_finalizers.append(_finalize_pokemons_encountered)


    def _get_unique_pokedex_entries(self):
        if 7 in self._cache:
            r = self._cache[7]
        else:
            r = self._buf_get(7, ProtoBase.TYPE_int32, 'unique_pokedex_entries')
            self._cache[7] = r
        return r

    def _establish_parentage_unique_pokedex_entries(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_unique_pokedex_entries), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_unique_pokedex_entries
                v._pbf_establish_parent_callback = self._establish_parentage_unique_pokedex_entries

    def _set_unique_pokedex_entries(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_unique_pokedex_entries(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field unique_pokedex_entries"
            raise ProtoValueError(list_assign_error)
        self._cache[7] = v
        self._mods[7] = ProtoBase.TYPE_int32

    def _mod_unique_pokedex_entries(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[7] = ProtoBase.TYPE_int32

    def _del_unique_pokedex_entries(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 7 in self._cache:
            del self._cache[7]
        if 7 in self._mods:
            del self._mods[7]
        self._buf_del(7)

    _pb_field_name_7 = "unique_pokedex_entries"

    unique_pokedex_entries = property(_get_unique_pokedex_entries, _set_unique_pokedex_entries, _del_unique_pokedex_entries)

    @property
    def unique_pokedex_entries__exists(self):
        return 7 in self._mods or self._buf_exists(7)

    @property
    def unique_pokedex_entries__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_unique_pokedex_entries(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(7)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(7)

    _pbf_finalizers.append(_finalize_unique_pokedex_entries)


    def _get_pokemons_captured(self):
        if 8 in self._cache:
            r = self._cache[8]
        else:
            r = self._buf_get(8, ProtoBase.TYPE_int32, 'pokemons_captured')
            self._cache[8] = r
        return r

    def _establish_parentage_pokemons_captured(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokemons_captured), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokemons_captured
                v._pbf_establish_parent_callback = self._establish_parentage_pokemons_captured

    def _set_pokemons_captured(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokemons_captured(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokemons_captured"
            raise ProtoValueError(list_assign_error)
        self._cache[8] = v
        self._mods[8] = ProtoBase.TYPE_int32

    def _mod_pokemons_captured(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[8] = ProtoBase.TYPE_int32

    def _del_pokemons_captured(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 8 in self._cache:
            del self._cache[8]
        if 8 in self._mods:
            del self._mods[8]
        self._buf_del(8)

    _pb_field_name_8 = "pokemons_captured"

    pokemons_captured = property(_get_pokemons_captured, _set_pokemons_captured, _del_pokemons_captured)

    @property
    def pokemons_captured__exists(self):
        return 8 in self._mods or self._buf_exists(8)

    @property
    def pokemons_captured__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_pokemons_captured(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(8)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(8)

    _pbf_finalizers.append(_finalize_pokemons_captured)


    def _get_evolutions(self):
        if 9 in self._cache:
            r = self._cache[9]
        else:
            r = self._buf_get(9, ProtoBase.TYPE_int32, 'evolutions')
            self._cache[9] = r
        return r

    def _establish_parentage_evolutions(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_evolutions), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_evolutions
                v._pbf_establish_parent_callback = self._establish_parentage_evolutions

    def _set_evolutions(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_evolutions(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field evolutions"
            raise ProtoValueError(list_assign_error)
        self._cache[9] = v
        self._mods[9] = ProtoBase.TYPE_int32

    def _mod_evolutions(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[9] = ProtoBase.TYPE_int32

    def _del_evolutions(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 9 in self._cache:
            del self._cache[9]
        if 9 in self._mods:
            del self._mods[9]
        self._buf_del(9)

    _pb_field_name_9 = "evolutions"

    evolutions = property(_get_evolutions, _set_evolutions, _del_evolutions)

    @property
    def evolutions__exists(self):
        return 9 in self._mods or self._buf_exists(9)

    @property
    def evolutions__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_evolutions(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(9)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(9)

    _pbf_finalizers.append(_finalize_evolutions)


    def _get_poke_stop_visits(self):
        if 10 in self._cache:
            r = self._cache[10]
        else:
            r = self._buf_get(10, ProtoBase.TYPE_int32, 'poke_stop_visits')
            self._cache[10] = r
        return r

    def _establish_parentage_poke_stop_visits(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_poke_stop_visits), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_poke_stop_visits
                v._pbf_establish_parent_callback = self._establish_parentage_poke_stop_visits

    def _set_poke_stop_visits(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_poke_stop_visits(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field poke_stop_visits"
            raise ProtoValueError(list_assign_error)
        self._cache[10] = v
        self._mods[10] = ProtoBase.TYPE_int32

    def _mod_poke_stop_visits(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[10] = ProtoBase.TYPE_int32

    def _del_poke_stop_visits(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 10 in self._cache:
            del self._cache[10]
        if 10 in self._mods:
            del self._mods[10]
        self._buf_del(10)

    _pb_field_name_10 = "poke_stop_visits"

    poke_stop_visits = property(_get_poke_stop_visits, _set_poke_stop_visits, _del_poke_stop_visits)

    @property
    def poke_stop_visits__exists(self):
        return 10 in self._mods or self._buf_exists(10)

    @property
    def poke_stop_visits__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_poke_stop_visits(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(10)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(10)

    _pbf_finalizers.append(_finalize_poke_stop_visits)


    def _get_pokeballs_thrown(self):
        if 11 in self._cache:
            r = self._cache[11]
        else:
            r = self._buf_get(11, ProtoBase.TYPE_int32, 'pokeballs_thrown')
            self._cache[11] = r
        return r

    def _establish_parentage_pokeballs_thrown(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokeballs_thrown), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokeballs_thrown
                v._pbf_establish_parent_callback = self._establish_parentage_pokeballs_thrown

    def _set_pokeballs_thrown(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokeballs_thrown(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokeballs_thrown"
            raise ProtoValueError(list_assign_error)
        self._cache[11] = v
        self._mods[11] = ProtoBase.TYPE_int32

    def _mod_pokeballs_thrown(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[11] = ProtoBase.TYPE_int32

    def _del_pokeballs_thrown(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 11 in self._cache:
            del self._cache[11]
        if 11 in self._mods:
            del self._mods[11]
        self._buf_del(11)

    _pb_field_name_11 = "pokeballs_thrown"

    pokeballs_thrown = property(_get_pokeballs_thrown, _set_pokeballs_thrown, _del_pokeballs_thrown)

    @property
    def pokeballs_thrown__exists(self):
        return 11 in self._mods or self._buf_exists(11)

    @property
    def pokeballs_thrown__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_pokeballs_thrown(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(11)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(11)

    _pbf_finalizers.append(_finalize_pokeballs_thrown)


    def _get_eggs_hatched(self):
        if 12 in self._cache:
            r = self._cache[12]
        else:
            r = self._buf_get(12, ProtoBase.TYPE_int32, 'eggs_hatched')
            self._cache[12] = r
        return r

    def _establish_parentage_eggs_hatched(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_eggs_hatched), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_eggs_hatched
                v._pbf_establish_parent_callback = self._establish_parentage_eggs_hatched

    def _set_eggs_hatched(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_eggs_hatched(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field eggs_hatched"
            raise ProtoValueError(list_assign_error)
        self._cache[12] = v
        self._mods[12] = ProtoBase.TYPE_int32

    def _mod_eggs_hatched(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[12] = ProtoBase.TYPE_int32

    def _del_eggs_hatched(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 12 in self._cache:
            del self._cache[12]
        if 12 in self._mods:
            del self._mods[12]
        self._buf_del(12)

    _pb_field_name_12 = "eggs_hatched"

    eggs_hatched = property(_get_eggs_hatched, _set_eggs_hatched, _del_eggs_hatched)

    @property
    def eggs_hatched__exists(self):
        return 12 in self._mods or self._buf_exists(12)

    @property
    def eggs_hatched__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_eggs_hatched(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(12)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(12)

    _pbf_finalizers.append(_finalize_eggs_hatched)


    def _get_big_magikarp_caught(self):
        if 13 in self._cache:
            r = self._cache[13]
        else:
            r = self._buf_get(13, ProtoBase.TYPE_int32, 'big_magikarp_caught')
            self._cache[13] = r
        return r

    def _establish_parentage_big_magikarp_caught(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_big_magikarp_caught), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_big_magikarp_caught
                v._pbf_establish_parent_callback = self._establish_parentage_big_magikarp_caught

    def _set_big_magikarp_caught(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_big_magikarp_caught(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field big_magikarp_caught"
            raise ProtoValueError(list_assign_error)
        self._cache[13] = v
        self._mods[13] = ProtoBase.TYPE_int32

    def _mod_big_magikarp_caught(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[13] = ProtoBase.TYPE_int32

    def _del_big_magikarp_caught(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 13 in self._cache:
            del self._cache[13]
        if 13 in self._mods:
            del self._mods[13]
        self._buf_del(13)

    _pb_field_name_13 = "big_magikarp_caught"

    big_magikarp_caught = property(_get_big_magikarp_caught, _set_big_magikarp_caught, _del_big_magikarp_caught)

    @property
    def big_magikarp_caught__exists(self):
        return 13 in self._mods or self._buf_exists(13)

    @property
    def big_magikarp_caught__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_big_magikarp_caught(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(13)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(13)

    _pbf_finalizers.append(_finalize_big_magikarp_caught)


    def _get_battle_attack_won(self):
        if 14 in self._cache:
            r = self._cache[14]
        else:
            r = self._buf_get(14, ProtoBase.TYPE_int32, 'battle_attack_won')
            self._cache[14] = r
        return r

    def _establish_parentage_battle_attack_won(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_battle_attack_won), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_battle_attack_won
                v._pbf_establish_parent_callback = self._establish_parentage_battle_attack_won

    def _set_battle_attack_won(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_battle_attack_won(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field battle_attack_won"
            raise ProtoValueError(list_assign_error)
        self._cache[14] = v
        self._mods[14] = ProtoBase.TYPE_int32

    def _mod_battle_attack_won(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[14] = ProtoBase.TYPE_int32

    def _del_battle_attack_won(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 14 in self._cache:
            del self._cache[14]
        if 14 in self._mods:
            del self._mods[14]
        self._buf_del(14)

    _pb_field_name_14 = "battle_attack_won"

    battle_attack_won = property(_get_battle_attack_won, _set_battle_attack_won, _del_battle_attack_won)

    @property
    def battle_attack_won__exists(self):
        return 14 in self._mods or self._buf_exists(14)

    @property
    def battle_attack_won__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_battle_attack_won(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(14)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(14)

    _pbf_finalizers.append(_finalize_battle_attack_won)


    def _get_battle_attack_total(self):
        if 15 in self._cache:
            r = self._cache[15]
        else:
            r = self._buf_get(15, ProtoBase.TYPE_int32, 'battle_attack_total')
            self._cache[15] = r
        return r

    def _establish_parentage_battle_attack_total(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_battle_attack_total), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_battle_attack_total
                v._pbf_establish_parent_callback = self._establish_parentage_battle_attack_total

    def _set_battle_attack_total(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_battle_attack_total(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field battle_attack_total"
            raise ProtoValueError(list_assign_error)
        self._cache[15] = v
        self._mods[15] = ProtoBase.TYPE_int32

    def _mod_battle_attack_total(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[15] = ProtoBase.TYPE_int32

    def _del_battle_attack_total(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 15 in self._cache:
            del self._cache[15]
        if 15 in self._mods:
            del self._mods[15]
        self._buf_del(15)

    _pb_field_name_15 = "battle_attack_total"

    battle_attack_total = property(_get_battle_attack_total, _set_battle_attack_total, _del_battle_attack_total)

    @property
    def battle_attack_total__exists(self):
        return 15 in self._mods or self._buf_exists(15)

    @property
    def battle_attack_total__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_battle_attack_total(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(15)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(15)

    _pbf_finalizers.append(_finalize_battle_attack_total)


    def _get_battle_defended_won(self):
        if 16 in self._cache:
            r = self._cache[16]
        else:
            r = self._buf_get(16, ProtoBase.TYPE_int32, 'battle_defended_won')
            self._cache[16] = r
        return r

    def _establish_parentage_battle_defended_won(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_battle_defended_won), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_battle_defended_won
                v._pbf_establish_parent_callback = self._establish_parentage_battle_defended_won

    def _set_battle_defended_won(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_battle_defended_won(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field battle_defended_won"
            raise ProtoValueError(list_assign_error)
        self._cache[16] = v
        self._mods[16] = ProtoBase.TYPE_int32

    def _mod_battle_defended_won(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[16] = ProtoBase.TYPE_int32

    def _del_battle_defended_won(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 16 in self._cache:
            del self._cache[16]
        if 16 in self._mods:
            del self._mods[16]
        self._buf_del(16)

    _pb_field_name_16 = "battle_defended_won"

    battle_defended_won = property(_get_battle_defended_won, _set_battle_defended_won, _del_battle_defended_won)

    @property
    def battle_defended_won__exists(self):
        return 16 in self._mods or self._buf_exists(16)

    @property
    def battle_defended_won__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_battle_defended_won(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(16)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(16)

    _pbf_finalizers.append(_finalize_battle_defended_won)


    def _get_battle_training_won(self):
        if 17 in self._cache:
            r = self._cache[17]
        else:
            r = self._buf_get(17, ProtoBase.TYPE_int32, 'battle_training_won')
            self._cache[17] = r
        return r

    def _establish_parentage_battle_training_won(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_battle_training_won), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_battle_training_won
                v._pbf_establish_parent_callback = self._establish_parentage_battle_training_won

    def _set_battle_training_won(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_battle_training_won(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field battle_training_won"
            raise ProtoValueError(list_assign_error)
        self._cache[17] = v
        self._mods[17] = ProtoBase.TYPE_int32

    def _mod_battle_training_won(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[17] = ProtoBase.TYPE_int32

    def _del_battle_training_won(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 17 in self._cache:
            del self._cache[17]
        if 17 in self._mods:
            del self._mods[17]
        self._buf_del(17)

    _pb_field_name_17 = "battle_training_won"

    battle_training_won = property(_get_battle_training_won, _set_battle_training_won, _del_battle_training_won)

    @property
    def battle_training_won__exists(self):
        return 17 in self._mods or self._buf_exists(17)

    @property
    def battle_training_won__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_battle_training_won(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(17)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(17)

    _pbf_finalizers.append(_finalize_battle_training_won)


    def _get_battle_training_total(self):
        if 18 in self._cache:
            r = self._cache[18]
        else:
            r = self._buf_get(18, ProtoBase.TYPE_int32, 'battle_training_total')
            self._cache[18] = r
        return r

    def _establish_parentage_battle_training_total(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_battle_training_total), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_battle_training_total
                v._pbf_establish_parent_callback = self._establish_parentage_battle_training_total

    def _set_battle_training_total(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_battle_training_total(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field battle_training_total"
            raise ProtoValueError(list_assign_error)
        self._cache[18] = v
        self._mods[18] = ProtoBase.TYPE_int32

    def _mod_battle_training_total(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[18] = ProtoBase.TYPE_int32

    def _del_battle_training_total(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 18 in self._cache:
            del self._cache[18]
        if 18 in self._mods:
            del self._mods[18]
        self._buf_del(18)

    _pb_field_name_18 = "battle_training_total"

    battle_training_total = property(_get_battle_training_total, _set_battle_training_total, _del_battle_training_total)

    @property
    def battle_training_total__exists(self):
        return 18 in self._mods or self._buf_exists(18)

    @property
    def battle_training_total__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_battle_training_total(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(18)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(18)

    _pbf_finalizers.append(_finalize_battle_training_total)


    def _get_prestige_raised_total(self):
        if 19 in self._cache:
            r = self._cache[19]
        else:
            r = self._buf_get(19, ProtoBase.TYPE_int32, 'prestige_raised_total')
            self._cache[19] = r
        return r

    def _establish_parentage_prestige_raised_total(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_prestige_raised_total), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_prestige_raised_total
                v._pbf_establish_parent_callback = self._establish_parentage_prestige_raised_total

    def _set_prestige_raised_total(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_prestige_raised_total(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field prestige_raised_total"
            raise ProtoValueError(list_assign_error)
        self._cache[19] = v
        self._mods[19] = ProtoBase.TYPE_int32

    def _mod_prestige_raised_total(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[19] = ProtoBase.TYPE_int32

    def _del_prestige_raised_total(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 19 in self._cache:
            del self._cache[19]
        if 19 in self._mods:
            del self._mods[19]
        self._buf_del(19)

    _pb_field_name_19 = "prestige_raised_total"

    prestige_raised_total = property(_get_prestige_raised_total, _set_prestige_raised_total, _del_prestige_raised_total)

    @property
    def prestige_raised_total__exists(self):
        return 19 in self._mods or self._buf_exists(19)

    @property
    def prestige_raised_total__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_prestige_raised_total(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(19)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(19)

    _pbf_finalizers.append(_finalize_prestige_raised_total)


    def _get_prestige_dropped_total(self):
        if 20 in self._cache:
            r = self._cache[20]
        else:
            r = self._buf_get(20, ProtoBase.TYPE_int32, 'prestige_dropped_total')
            self._cache[20] = r
        return r

    def _establish_parentage_prestige_dropped_total(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_prestige_dropped_total), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_prestige_dropped_total
                v._pbf_establish_parent_callback = self._establish_parentage_prestige_dropped_total

    def _set_prestige_dropped_total(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_prestige_dropped_total(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field prestige_dropped_total"
            raise ProtoValueError(list_assign_error)
        self._cache[20] = v
        self._mods[20] = ProtoBase.TYPE_int32

    def _mod_prestige_dropped_total(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[20] = ProtoBase.TYPE_int32

    def _del_prestige_dropped_total(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 20 in self._cache:
            del self._cache[20]
        if 20 in self._mods:
            del self._mods[20]
        self._buf_del(20)

    _pb_field_name_20 = "prestige_dropped_total"

    prestige_dropped_total = property(_get_prestige_dropped_total, _set_prestige_dropped_total, _del_prestige_dropped_total)

    @property
    def prestige_dropped_total__exists(self):
        return 20 in self._mods or self._buf_exists(20)

    @property
    def prestige_dropped_total__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_prestige_dropped_total(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(20)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(20)

    _pbf_finalizers.append(_finalize_prestige_dropped_total)


    def _get_pokemon_deployed(self):
        if 21 in self._cache:
            r = self._cache[21]
        else:
            r = self._buf_get(21, ProtoBase.TYPE_int32, 'pokemon_deployed')
            self._cache[21] = r
        return r

    def _establish_parentage_pokemon_deployed(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokemon_deployed), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokemon_deployed
                v._pbf_establish_parent_callback = self._establish_parentage_pokemon_deployed

    def _set_pokemon_deployed(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokemon_deployed(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokemon_deployed"
            raise ProtoValueError(list_assign_error)
        self._cache[21] = v
        self._mods[21] = ProtoBase.TYPE_int32

    def _mod_pokemon_deployed(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[21] = ProtoBase.TYPE_int32

    def _del_pokemon_deployed(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 21 in self._cache:
            del self._cache[21]
        if 21 in self._mods:
            del self._mods[21]
        self._buf_del(21)

    _pb_field_name_21 = "pokemon_deployed"

    pokemon_deployed = property(_get_pokemon_deployed, _set_pokemon_deployed, _del_pokemon_deployed)

    @property
    def pokemon_deployed__exists(self):
        return 21 in self._mods or self._buf_exists(21)

    @property
    def pokemon_deployed__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_pokemon_deployed(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(21)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(21)

    _pbf_finalizers.append(_finalize_pokemon_deployed)


    def _get_pokemon_caught_by_type(self):
        if 22 in self._cache:
            r = self._cache[22]
        else:
            r = self._buf_get(22, ProtoBase.TYPE_bytes, 'pokemon_caught_by_type')
            self._cache[22] = r
        return r

    def _establish_parentage_pokemon_caught_by_type(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokemon_caught_by_type), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokemon_caught_by_type
                v._pbf_establish_parent_callback = self._establish_parentage_pokemon_caught_by_type

    def _set_pokemon_caught_by_type(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokemon_caught_by_type(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokemon_caught_by_type"
            raise ProtoValueError(list_assign_error)
        self._cache[22] = v
        self._mods[22] = ProtoBase.TYPE_bytes

    def _mod_pokemon_caught_by_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[22] = ProtoBase.TYPE_bytes

    def _del_pokemon_caught_by_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 22 in self._cache:
            del self._cache[22]
        if 22 in self._mods:
            del self._mods[22]
        self._buf_del(22)

    _pb_field_name_22 = "pokemon_caught_by_type"

    pokemon_caught_by_type = property(_get_pokemon_caught_by_type, _set_pokemon_caught_by_type, _del_pokemon_caught_by_type)

    @property
    def pokemon_caught_by_type__exists(self):
        return 22 in self._mods or self._buf_exists(22)

    @property
    def pokemon_caught_by_type__type(self):
        return ProtoBase.TYPE_bytes

    def _finalize_pokemon_caught_by_type(cls):
        if is_string(ProtoBase.TYPE_bytes):
            cls._pbf_strings.append(22)
        elif _PB_type(ProtoBase.TYPE_bytes) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bytes, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bytes.pb_subtype):
                cls._pbf_strings.append(22)

    _pbf_finalizers.append(_finalize_pokemon_caught_by_type)


    def _get_small_rattata_caught(self):
        if 23 in self._cache:
            r = self._cache[23]
        else:
            r = self._buf_get(23, ProtoBase.TYPE_int32, 'small_rattata_caught')
            self._cache[23] = r
        return r

    def _establish_parentage_small_rattata_caught(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_small_rattata_caught), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_small_rattata_caught
                v._pbf_establish_parent_callback = self._establish_parentage_small_rattata_caught

    def _set_small_rattata_caught(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_small_rattata_caught(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field small_rattata_caught"
            raise ProtoValueError(list_assign_error)
        self._cache[23] = v
        self._mods[23] = ProtoBase.TYPE_int32

    def _mod_small_rattata_caught(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[23] = ProtoBase.TYPE_int32

    def _del_small_rattata_caught(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 23 in self._cache:
            del self._cache[23]
        if 23 in self._mods:
            del self._mods[23]
        self._buf_del(23)

    _pb_field_name_23 = "small_rattata_caught"

    small_rattata_caught = property(_get_small_rattata_caught, _set_small_rattata_caught, _del_small_rattata_caught)

    @property
    def small_rattata_caught__exists(self):
        return 23 in self._mods or self._buf_exists(23)

    @property
    def small_rattata_caught__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_small_rattata_caught(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(23)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(23)

    _pbf_finalizers.append(_finalize_small_rattata_caught)


TYPE_PlayerStats = PlayerStats
_PB_finalizers.append('PlayerStats')

class PlayerCurrency(ProtoBase):
    _required = []
    _field_map = {'gems': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['gems']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_gems(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_int32, 'gems')
            self._cache[1] = r
        return r

    def _establish_parentage_gems(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_gems), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_gems
                v._pbf_establish_parent_callback = self._establish_parentage_gems

    def _set_gems(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_gems(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field gems"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_int32

    def _mod_gems(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_int32

    def _del_gems(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "gems"

    gems = property(_get_gems, _set_gems, _del_gems)

    @property
    def gems__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def gems__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_gems(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_gems)


TYPE_PlayerCurrency = PlayerCurrency
_PB_finalizers.append('PlayerCurrency')

class PlayerCamera(ProtoBase):
    _required = []
    _field_map = {'is_default_camera': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['is_default_camera']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_is_default_camera(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_bool, 'is_default_camera')
            self._cache[1] = r
        return r

    def _establish_parentage_is_default_camera(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_is_default_camera), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_is_default_camera
                v._pbf_establish_parent_callback = self._establish_parentage_is_default_camera

    def _set_is_default_camera(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_is_default_camera(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field is_default_camera"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_bool

    def _mod_is_default_camera(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_bool

    def _del_is_default_camera(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "is_default_camera"

    is_default_camera = property(_get_is_default_camera, _set_is_default_camera, _del_is_default_camera)

    @property
    def is_default_camera__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def is_default_camera__type(self):
        return ProtoBase.TYPE_bool

    def _finalize_is_default_camera(cls):
        if is_string(ProtoBase.TYPE_bool):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_bool) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bool, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bool.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_is_default_camera)


TYPE_PlayerCamera = PlayerCamera
_PB_finalizers.append('PlayerCamera')

class InventoryUpgrades(ProtoBase):
    _required = []
    _field_map = {'inventory_upgrades': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['inventory_upgrades']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    class Repeated_inventory_upgrades(RepeatedSequence):
        class pb_subtype(object):
            def __get__(self, instance, cls):
                return TYPE_InventoryUpgrade
        pb_subtype = pb_subtype()


    TYPE_Repeated_inventory_upgrades = Repeated_inventory_upgrades


    @property
    def inventory_upgrades__stream(self):
        if 1 in self._cache:
            def acc(v):
                v_ = lambda: v
                return v_
            return [acc(v) for v in self._cache[1]]
        return self._get_repeated(1, self.TYPE_Repeated_inventory_upgrades, "inventory_upgrades", lazy=True)

    def inventory_upgrades__fast_append(self, value):
        self._append_to_repeated(1, self.TYPE_Repeated_inventory_upgrades, value)

    def _get_inventory_upgrades(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, self.TYPE_Repeated_inventory_upgrades, 'inventory_upgrades')
            self._cache[1] = r
        return r

    def _establish_parentage_inventory_upgrades(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_inventory_upgrades), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_inventory_upgrades
                v._pbf_establish_parent_callback = self._establish_parentage_inventory_upgrades

    def _set_inventory_upgrades(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_inventory_upgrades(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field inventory_upgrades"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = self.TYPE_Repeated_inventory_upgrades

    def _mod_inventory_upgrades(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = self.TYPE_Repeated_inventory_upgrades

    def _del_inventory_upgrades(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "inventory_upgrades"

    inventory_upgrades = property(_get_inventory_upgrades, _set_inventory_upgrades, _del_inventory_upgrades)

    @property
    def inventory_upgrades__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def inventory_upgrades__type(self):
        return self.TYPE_Repeated_inventory_upgrades

    def _finalize_inventory_upgrades(cls):
        if is_string(cls.TYPE_Repeated_inventory_upgrades):
            cls._pbf_strings.append(1)
        elif _PB_type(cls.TYPE_Repeated_inventory_upgrades) is _PB_type:
            assert issubclass(cls.TYPE_Repeated_inventory_upgrades, RepeatedSequence)
            if is_string(cls.TYPE_Repeated_inventory_upgrades.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_inventory_upgrades)


TYPE_InventoryUpgrades = InventoryUpgrades
_PB_finalizers.append('InventoryUpgrades')

class InventoryUpgrade(ProtoBase):
    _required = []
    _field_map = {'item': 1, 'additional_storage': 3, 'upgrade_type': 2}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['item', 'upgrade_type', 'additional_storage']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_item(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, RpcEnum_palm.TYPE_ItemType, 'item')
            self._cache[1] = r
        return r

    def _establish_parentage_item(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_item), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_item
                v._pbf_establish_parent_callback = self._establish_parentage_item

    def _set_item(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_item(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field item"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = RpcEnum_palm.TYPE_ItemType

    def _mod_item(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = RpcEnum_palm.TYPE_ItemType

    def _del_item(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "item"

    item = property(_get_item, _set_item, _del_item)

    @property
    def item__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def item__type(self):
        return RpcEnum_palm.TYPE_ItemType

    def _finalize_item(cls):
        if is_string(RpcEnum_palm.TYPE_ItemType):
            cls._pbf_strings.append(1)
        elif _PB_type(RpcEnum_palm.TYPE_ItemType) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_ItemType, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_ItemType.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_item)


    def _get_upgrade_type(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, RpcEnum_palm.TYPE_InventoryUpgradeType, 'upgrade_type')
            self._cache[2] = r
        return r

    def _establish_parentage_upgrade_type(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_upgrade_type), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_upgrade_type
                v._pbf_establish_parent_callback = self._establish_parentage_upgrade_type

    def _set_upgrade_type(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_upgrade_type(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field upgrade_type"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = RpcEnum_palm.TYPE_InventoryUpgradeType

    def _mod_upgrade_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = RpcEnum_palm.TYPE_InventoryUpgradeType

    def _del_upgrade_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "upgrade_type"

    upgrade_type = property(_get_upgrade_type, _set_upgrade_type, _del_upgrade_type)

    @property
    def upgrade_type__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def upgrade_type__type(self):
        return RpcEnum_palm.TYPE_InventoryUpgradeType

    def _finalize_upgrade_type(cls):
        if is_string(RpcEnum_palm.TYPE_InventoryUpgradeType):
            cls._pbf_strings.append(2)
        elif _PB_type(RpcEnum_palm.TYPE_InventoryUpgradeType) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_InventoryUpgradeType, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_InventoryUpgradeType.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_upgrade_type)


    def _get_additional_storage(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_int32, 'additional_storage')
            self._cache[3] = r
        return r

    def _establish_parentage_additional_storage(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_additional_storage), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_additional_storage
                v._pbf_establish_parent_callback = self._establish_parentage_additional_storage

    def _set_additional_storage(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_additional_storage(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field additional_storage"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_int32

    def _mod_additional_storage(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_int32

    def _del_additional_storage(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "additional_storage"

    additional_storage = property(_get_additional_storage, _set_additional_storage, _del_additional_storage)

    @property
    def additional_storage__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def additional_storage__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_additional_storage(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_additional_storage)


TYPE_InventoryUpgrade = InventoryUpgrade
_PB_finalizers.append('InventoryUpgrade')

class AppliedItems(ProtoBase):
    _required = []
    _field_map = {'item': 4}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['item']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_item(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, TYPE_AppliedItem, 'item')
            self._cache[4] = r
        return r

    def _establish_parentage_item(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_item), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_item
                v._pbf_establish_parent_callback = self._establish_parentage_item

    def _set_item(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_item(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field item"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = TYPE_AppliedItem

    def _mod_item(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = TYPE_AppliedItem

    def _del_item(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "item"

    item = property(_get_item, _set_item, _del_item)

    @property
    def item__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def item__type(self):
        return TYPE_AppliedItem

    def _finalize_item(cls):
        if is_string(TYPE_AppliedItem):
            cls._pbf_strings.append(4)
        elif _PB_type(TYPE_AppliedItem) is _PB_type:
            assert issubclass(TYPE_AppliedItem, RepeatedSequence)
            if is_string(TYPE_AppliedItem.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_item)


TYPE_AppliedItems = AppliedItems
_PB_finalizers.append('AppliedItems')

class AppliedItem(ProtoBase):
    _required = []
    _field_map = {'applied_ms': 4, 'item_type': 1, 'expire_ms': 3, 'item_type_category': 2}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['item_type', 'item_type_category', 'expire_ms', 'applied_ms']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_item_type(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, RpcEnum_palm.TYPE_ItemType, 'item_type')
            self._cache[1] = r
        return r

    def _establish_parentage_item_type(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_item_type), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_item_type
                v._pbf_establish_parent_callback = self._establish_parentage_item_type

    def _set_item_type(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_item_type(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field item_type"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = RpcEnum_palm.TYPE_ItemType

    def _mod_item_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = RpcEnum_palm.TYPE_ItemType

    def _del_item_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "item_type"

    item_type = property(_get_item_type, _set_item_type, _del_item_type)

    @property
    def item_type__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def item_type__type(self):
        return RpcEnum_palm.TYPE_ItemType

    def _finalize_item_type(cls):
        if is_string(RpcEnum_palm.TYPE_ItemType):
            cls._pbf_strings.append(1)
        elif _PB_type(RpcEnum_palm.TYPE_ItemType) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_ItemType, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_ItemType.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_item_type)


    def _get_item_type_category(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, RpcEnum_palm.TYPE_ItemTypeCategory, 'item_type_category')
            self._cache[2] = r
        return r

    def _establish_parentage_item_type_category(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_item_type_category), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_item_type_category
                v._pbf_establish_parent_callback = self._establish_parentage_item_type_category

    def _set_item_type_category(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_item_type_category(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field item_type_category"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = RpcEnum_palm.TYPE_ItemTypeCategory

    def _mod_item_type_category(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = RpcEnum_palm.TYPE_ItemTypeCategory

    def _del_item_type_category(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "item_type_category"

    item_type_category = property(_get_item_type_category, _set_item_type_category, _del_item_type_category)

    @property
    def item_type_category__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def item_type_category__type(self):
        return RpcEnum_palm.TYPE_ItemTypeCategory

    def _finalize_item_type_category(cls):
        if is_string(RpcEnum_palm.TYPE_ItemTypeCategory):
            cls._pbf_strings.append(2)
        elif _PB_type(RpcEnum_palm.TYPE_ItemTypeCategory) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_ItemTypeCategory, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_ItemTypeCategory.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_item_type_category)


    def _get_expire_ms(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_int64, 'expire_ms')
            self._cache[3] = r
        return r

    def _establish_parentage_expire_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_expire_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_expire_ms
                v._pbf_establish_parent_callback = self._establish_parentage_expire_ms

    def _set_expire_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_expire_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field expire_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_int64

    def _mod_expire_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_int64

    def _del_expire_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "expire_ms"

    expire_ms = property(_get_expire_ms, _set_expire_ms, _del_expire_ms)

    @property
    def expire_ms__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def expire_ms__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_expire_ms(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_expire_ms)


    def _get_applied_ms(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, ProtoBase.TYPE_int64, 'applied_ms')
            self._cache[4] = r
        return r

    def _establish_parentage_applied_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_applied_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_applied_ms
                v._pbf_establish_parent_callback = self._establish_parentage_applied_ms

    def _set_applied_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_applied_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field applied_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = ProtoBase.TYPE_int64

    def _mod_applied_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = ProtoBase.TYPE_int64

    def _del_applied_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "applied_ms"

    applied_ms = property(_get_applied_ms, _set_applied_ms, _del_applied_ms)

    @property
    def applied_ms__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def applied_ms__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_applied_ms(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(4)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_applied_ms)


TYPE_AppliedItem = AppliedItem
_PB_finalizers.append('AppliedItem')

class EggIncubators(ProtoBase):
    _required = []
    _field_map = {'egg_incubator': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['egg_incubator']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_egg_incubator(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, TYPE_EggIncubator, 'egg_incubator')
            self._cache[1] = r
        return r

    def _establish_parentage_egg_incubator(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_egg_incubator), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_egg_incubator
                v._pbf_establish_parent_callback = self._establish_parentage_egg_incubator

    def _set_egg_incubator(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_egg_incubator(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field egg_incubator"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = TYPE_EggIncubator

    def _mod_egg_incubator(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = TYPE_EggIncubator

    def _del_egg_incubator(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "egg_incubator"

    egg_incubator = property(_get_egg_incubator, _set_egg_incubator, _del_egg_incubator)

    @property
    def egg_incubator__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def egg_incubator__type(self):
        return TYPE_EggIncubator

    def _finalize_egg_incubator(cls):
        if is_string(TYPE_EggIncubator):
            cls._pbf_strings.append(1)
        elif _PB_type(TYPE_EggIncubator) is _PB_type:
            assert issubclass(TYPE_EggIncubator, RepeatedSequence)
            if is_string(TYPE_EggIncubator.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_egg_incubator)


TYPE_EggIncubators = EggIncubators
_PB_finalizers.append('EggIncubators')

class EggIncubator(ProtoBase):
    _required = []
    _field_map = {'target_km_walked': 7, 'pokemon_id': 5, 'start_km_walked': 6, 'uses_remaining': 4, 'item_type': 2, 'incubator_type': 3, 'item_id': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['item_id', 'item_type', 'incubator_type', 'uses_remaining', 'pokemon_id', 'start_km_walked', 'target_km_walked']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_item_id(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_string, 'item_id')
            self._cache[1] = r
        return r

    def _establish_parentage_item_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_item_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_item_id
                v._pbf_establish_parent_callback = self._establish_parentage_item_id

    def _set_item_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_item_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field item_id"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_string

    def _mod_item_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_string

    def _del_item_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "item_id"

    item_id = property(_get_item_id, _set_item_id, _del_item_id)

    @property
    def item_id__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def item_id__type(self):
        return ProtoBase.TYPE_string

    def _finalize_item_id(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_item_id)


    def _get_item_type(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, RpcEnum_palm.TYPE_ItemType, 'item_type')
            self._cache[2] = r
        return r

    def _establish_parentage_item_type(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_item_type), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_item_type
                v._pbf_establish_parent_callback = self._establish_parentage_item_type

    def _set_item_type(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_item_type(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field item_type"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = RpcEnum_palm.TYPE_ItemType

    def _mod_item_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = RpcEnum_palm.TYPE_ItemType

    def _del_item_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "item_type"

    item_type = property(_get_item_type, _set_item_type, _del_item_type)

    @property
    def item_type__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def item_type__type(self):
        return RpcEnum_palm.TYPE_ItemType

    def _finalize_item_type(cls):
        if is_string(RpcEnum_palm.TYPE_ItemType):
            cls._pbf_strings.append(2)
        elif _PB_type(RpcEnum_palm.TYPE_ItemType) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_ItemType, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_ItemType.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_item_type)


    def _get_incubator_type(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, RpcEnum_palm.TYPE_EggIncubatorType, 'incubator_type')
            self._cache[3] = r
        return r

    def _establish_parentage_incubator_type(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_incubator_type), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_incubator_type
                v._pbf_establish_parent_callback = self._establish_parentage_incubator_type

    def _set_incubator_type(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_incubator_type(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field incubator_type"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = RpcEnum_palm.TYPE_EggIncubatorType

    def _mod_incubator_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = RpcEnum_palm.TYPE_EggIncubatorType

    def _del_incubator_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "incubator_type"

    incubator_type = property(_get_incubator_type, _set_incubator_type, _del_incubator_type)

    @property
    def incubator_type__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def incubator_type__type(self):
        return RpcEnum_palm.TYPE_EggIncubatorType

    def _finalize_incubator_type(cls):
        if is_string(RpcEnum_palm.TYPE_EggIncubatorType):
            cls._pbf_strings.append(3)
        elif _PB_type(RpcEnum_palm.TYPE_EggIncubatorType) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_EggIncubatorType, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_EggIncubatorType.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_incubator_type)


    def _get_uses_remaining(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, ProtoBase.TYPE_int32, 'uses_remaining')
            self._cache[4] = r
        return r

    def _establish_parentage_uses_remaining(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_uses_remaining), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_uses_remaining
                v._pbf_establish_parent_callback = self._establish_parentage_uses_remaining

    def _set_uses_remaining(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_uses_remaining(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field uses_remaining"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = ProtoBase.TYPE_int32

    def _mod_uses_remaining(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = ProtoBase.TYPE_int32

    def _del_uses_remaining(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "uses_remaining"

    uses_remaining = property(_get_uses_remaining, _set_uses_remaining, _del_uses_remaining)

    @property
    def uses_remaining__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def uses_remaining__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_uses_remaining(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(4)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_uses_remaining)


    def _get_pokemon_id(self):
        if 5 in self._cache:
            r = self._cache[5]
        else:
            r = self._buf_get(5, ProtoBase.TYPE_int64, 'pokemon_id')
            self._cache[5] = r
        return r

    def _establish_parentage_pokemon_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokemon_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokemon_id
                v._pbf_establish_parent_callback = self._establish_parentage_pokemon_id

    def _set_pokemon_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokemon_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokemon_id"
            raise ProtoValueError(list_assign_error)
        self._cache[5] = v
        self._mods[5] = ProtoBase.TYPE_int64

    def _mod_pokemon_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[5] = ProtoBase.TYPE_int64

    def _del_pokemon_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 5 in self._cache:
            del self._cache[5]
        if 5 in self._mods:
            del self._mods[5]
        self._buf_del(5)

    _pb_field_name_5 = "pokemon_id"

    pokemon_id = property(_get_pokemon_id, _set_pokemon_id, _del_pokemon_id)

    @property
    def pokemon_id__exists(self):
        return 5 in self._mods or self._buf_exists(5)

    @property
    def pokemon_id__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_pokemon_id(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(5)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(5)

    _pbf_finalizers.append(_finalize_pokemon_id)


    def _get_start_km_walked(self):
        if 6 in self._cache:
            r = self._cache[6]
        else:
            r = self._buf_get(6, ProtoBase.TYPE_double, 'start_km_walked')
            self._cache[6] = r
        return r

    def _establish_parentage_start_km_walked(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_start_km_walked), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_start_km_walked
                v._pbf_establish_parent_callback = self._establish_parentage_start_km_walked

    def _set_start_km_walked(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_start_km_walked(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field start_km_walked"
            raise ProtoValueError(list_assign_error)
        self._cache[6] = v
        self._mods[6] = ProtoBase.TYPE_double

    def _mod_start_km_walked(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[6] = ProtoBase.TYPE_double

    def _del_start_km_walked(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 6 in self._cache:
            del self._cache[6]
        if 6 in self._mods:
            del self._mods[6]
        self._buf_del(6)

    _pb_field_name_6 = "start_km_walked"

    start_km_walked = property(_get_start_km_walked, _set_start_km_walked, _del_start_km_walked)

    @property
    def start_km_walked__exists(self):
        return 6 in self._mods or self._buf_exists(6)

    @property
    def start_km_walked__type(self):
        return ProtoBase.TYPE_double

    def _finalize_start_km_walked(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(6)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(6)

    _pbf_finalizers.append(_finalize_start_km_walked)


    def _get_target_km_walked(self):
        if 7 in self._cache:
            r = self._cache[7]
        else:
            r = self._buf_get(7, ProtoBase.TYPE_double, 'target_km_walked')
            self._cache[7] = r
        return r

    def _establish_parentage_target_km_walked(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_target_km_walked), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_target_km_walked
                v._pbf_establish_parent_callback = self._establish_parentage_target_km_walked

    def _set_target_km_walked(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_target_km_walked(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field target_km_walked"
            raise ProtoValueError(list_assign_error)
        self._cache[7] = v
        self._mods[7] = ProtoBase.TYPE_double

    def _mod_target_km_walked(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[7] = ProtoBase.TYPE_double

    def _del_target_km_walked(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 7 in self._cache:
            del self._cache[7]
        if 7 in self._mods:
            del self._mods[7]
        self._buf_del(7)

    _pb_field_name_7 = "target_km_walked"

    target_km_walked = property(_get_target_km_walked, _set_target_km_walked, _del_target_km_walked)

    @property
    def target_km_walked__exists(self):
        return 7 in self._mods or self._buf_exists(7)

    @property
    def target_km_walked__type(self):
        return ProtoBase.TYPE_double

    def _finalize_target_km_walked(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(7)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(7)

    _pbf_finalizers.append(_finalize_target_km_walked)


TYPE_EggIncubator = EggIncubator
_PB_finalizers.append('EggIncubator')

class PokemonFamily(ProtoBase):
    _required = []
    _field_map = {'family_id': 1, 'candy': 2}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['family_id', 'candy']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_family_id(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, RpcEnum_palm.TYPE_PokemonFamilyId, 'family_id')
            self._cache[1] = r
        return r

    def _establish_parentage_family_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_family_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_family_id
                v._pbf_establish_parent_callback = self._establish_parentage_family_id

    def _set_family_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_family_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field family_id"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = RpcEnum_palm.TYPE_PokemonFamilyId

    def _mod_family_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = RpcEnum_palm.TYPE_PokemonFamilyId

    def _del_family_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "family_id"

    family_id = property(_get_family_id, _set_family_id, _del_family_id)

    @property
    def family_id__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def family_id__type(self):
        return RpcEnum_palm.TYPE_PokemonFamilyId

    def _finalize_family_id(cls):
        if is_string(RpcEnum_palm.TYPE_PokemonFamilyId):
            cls._pbf_strings.append(1)
        elif _PB_type(RpcEnum_palm.TYPE_PokemonFamilyId) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_PokemonFamilyId, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_PokemonFamilyId.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_family_id)


    def _get_candy(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int32, 'candy')
            self._cache[2] = r
        return r

    def _establish_parentage_candy(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_candy), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_candy
                v._pbf_establish_parent_callback = self._establish_parentage_candy

    def _set_candy(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_candy(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field candy"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_int32

    def _mod_candy(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int32

    def _del_candy(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "candy"

    candy = property(_get_candy, _set_candy, _del_candy)

    @property
    def candy__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def candy__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_candy(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_candy)


TYPE_PokemonFamily = PokemonFamily
_PB_finalizers.append('PokemonFamily')

class GetMapObjectsRequest(ProtoBase):
    _required = []
    _field_map = {'since_timestamp_ms': 2, 'latitude': 3, 'cell_id': 1, 'longitude': 4}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['cell_id', 'since_timestamp_ms', 'latitude', 'longitude']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_cell_id(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_bytes, 'cell_id')
            self._cache[1] = r
        return r

    def _establish_parentage_cell_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_cell_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_cell_id
                v._pbf_establish_parent_callback = self._establish_parentage_cell_id

    def _set_cell_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_cell_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field cell_id"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_bytes

    def _mod_cell_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_bytes

    def _del_cell_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "cell_id"

    cell_id = property(_get_cell_id, _set_cell_id, _del_cell_id)

    @property
    def cell_id__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def cell_id__type(self):
        return ProtoBase.TYPE_bytes

    def _finalize_cell_id(cls):
        if is_string(ProtoBase.TYPE_bytes):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_bytes) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bytes, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bytes.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_cell_id)


    def _get_since_timestamp_ms(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_bytes, 'since_timestamp_ms')
            self._cache[2] = r
        return r

    def _establish_parentage_since_timestamp_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_since_timestamp_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_since_timestamp_ms
                v._pbf_establish_parent_callback = self._establish_parentage_since_timestamp_ms

    def _set_since_timestamp_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_since_timestamp_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field since_timestamp_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_bytes

    def _mod_since_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_bytes

    def _del_since_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "since_timestamp_ms"

    since_timestamp_ms = property(_get_since_timestamp_ms, _set_since_timestamp_ms, _del_since_timestamp_ms)

    @property
    def since_timestamp_ms__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def since_timestamp_ms__type(self):
        return ProtoBase.TYPE_bytes

    def _finalize_since_timestamp_ms(cls):
        if is_string(ProtoBase.TYPE_bytes):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_bytes) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bytes, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bytes.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_since_timestamp_ms)


    def _get_latitude(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_double, 'latitude')
            self._cache[3] = r
        return r

    def _establish_parentage_latitude(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_latitude), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_latitude
                v._pbf_establish_parent_callback = self._establish_parentage_latitude

    def _set_latitude(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_latitude(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field latitude"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_double

    def _mod_latitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_double

    def _del_latitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "latitude"

    latitude = property(_get_latitude, _set_latitude, _del_latitude)

    @property
    def latitude__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def latitude__type(self):
        return ProtoBase.TYPE_double

    def _finalize_latitude(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_latitude)


    def _get_longitude(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, ProtoBase.TYPE_double, 'longitude')
            self._cache[4] = r
        return r

    def _establish_parentage_longitude(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_longitude), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_longitude
                v._pbf_establish_parent_callback = self._establish_parentage_longitude

    def _set_longitude(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_longitude(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field longitude"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = ProtoBase.TYPE_double

    def _mod_longitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = ProtoBase.TYPE_double

    def _del_longitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "longitude"

    longitude = property(_get_longitude, _set_longitude, _del_longitude)

    @property
    def longitude__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def longitude__type(self):
        return ProtoBase.TYPE_double

    def _finalize_longitude(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(4)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_longitude)


TYPE_GetMapObjectsRequest = GetMapObjectsRequest
_PB_finalizers.append('GetMapObjectsRequest')

class GetMapObjectsResponse(ProtoBase):
    _required = []
    _field_map = {'status': 2, 'map_cells': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['map_cells', 'status']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    class Repeated_map_cells(RepeatedSequence):
        class pb_subtype(object):
            def __get__(self, instance, cls):
                return TYPE_MapCell
        pb_subtype = pb_subtype()


    TYPE_Repeated_map_cells = Repeated_map_cells


    @property
    def map_cells__stream(self):
        if 1 in self._cache:
            def acc(v):
                v_ = lambda: v
                return v_
            return [acc(v) for v in self._cache[1]]
        return self._get_repeated(1, self.TYPE_Repeated_map_cells, "map_cells", lazy=True)

    def map_cells__fast_append(self, value):
        self._append_to_repeated(1, self.TYPE_Repeated_map_cells, value)

    def _get_map_cells(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, self.TYPE_Repeated_map_cells, 'map_cells')
            self._cache[1] = r
        return r

    def _establish_parentage_map_cells(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_map_cells), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_map_cells
                v._pbf_establish_parent_callback = self._establish_parentage_map_cells

    def _set_map_cells(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_map_cells(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field map_cells"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = self.TYPE_Repeated_map_cells

    def _mod_map_cells(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = self.TYPE_Repeated_map_cells

    def _del_map_cells(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "map_cells"

    map_cells = property(_get_map_cells, _set_map_cells, _del_map_cells)

    @property
    def map_cells__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def map_cells__type(self):
        return self.TYPE_Repeated_map_cells

    def _finalize_map_cells(cls):
        if is_string(cls.TYPE_Repeated_map_cells):
            cls._pbf_strings.append(1)
        elif _PB_type(cls.TYPE_Repeated_map_cells) is _PB_type:
            assert issubclass(cls.TYPE_Repeated_map_cells, RepeatedSequence)
            if is_string(cls.TYPE_Repeated_map_cells.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_map_cells)


    def _get_status(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, RpcEnum_palm.TYPE_MapObjectsStatus, 'status')
            self._cache[2] = r
        return r

    def _establish_parentage_status(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_status), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_status
                v._pbf_establish_parent_callback = self._establish_parentage_status

    def _set_status(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_status(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field status"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = RpcEnum_palm.TYPE_MapObjectsStatus

    def _mod_status(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = RpcEnum_palm.TYPE_MapObjectsStatus

    def _del_status(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "status"

    status = property(_get_status, _set_status, _del_status)

    @property
    def status__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def status__type(self):
        return RpcEnum_palm.TYPE_MapObjectsStatus

    def _finalize_status(cls):
        if is_string(RpcEnum_palm.TYPE_MapObjectsStatus):
            cls._pbf_strings.append(2)
        elif _PB_type(RpcEnum_palm.TYPE_MapObjectsStatus) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_MapObjectsStatus, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_MapObjectsStatus.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_status)


TYPE_GetMapObjectsResponse = GetMapObjectsResponse
_PB_finalizers.append('GetMapObjectsResponse')

class MapCell(ProtoBase):
    _required = []
    _field_map = {'nearby_pokemons': 11, 'fort_summaries': 8, 'decimated_spawn_points': 9, 'forts': 3, 'spawn_points': 4, 'is_truncated_list': 7, 'catchable_pokemons': 10, 'wild_pokemons': 5, 'current_timestamp_ms': 2, 'deleted_objects': 6, 's2_cell_id': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['s2_cell_id', 'current_timestamp_ms', 'forts', 'spawn_points', 'wild_pokemons', 'deleted_objects', 'is_truncated_list', 'fort_summaries', 'decimated_spawn_points', 'catchable_pokemons', 'nearby_pokemons']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_s2_cell_id(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_uint64, 's2_cell_id')
            self._cache[1] = r
        return r

    def _establish_parentage_s2_cell_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_s2_cell_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_s2_cell_id
                v._pbf_establish_parent_callback = self._establish_parentage_s2_cell_id

    def _set_s2_cell_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_s2_cell_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field s2_cell_id"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_uint64

    def _mod_s2_cell_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_uint64

    def _del_s2_cell_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "s2_cell_id"

    s2_cell_id = property(_get_s2_cell_id, _set_s2_cell_id, _del_s2_cell_id)

    @property
    def s2_cell_id__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def s2_cell_id__type(self):
        return ProtoBase.TYPE_uint64

    def _finalize_s2_cell_id(cls):
        if is_string(ProtoBase.TYPE_uint64):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_uint64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_uint64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_uint64.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_s2_cell_id)


    def _get_current_timestamp_ms(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int64, 'current_timestamp_ms')
            self._cache[2] = r
        return r

    def _establish_parentage_current_timestamp_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_current_timestamp_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_current_timestamp_ms
                v._pbf_establish_parent_callback = self._establish_parentage_current_timestamp_ms

    def _set_current_timestamp_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_current_timestamp_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field current_timestamp_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_int64

    def _mod_current_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int64

    def _del_current_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "current_timestamp_ms"

    current_timestamp_ms = property(_get_current_timestamp_ms, _set_current_timestamp_ms, _del_current_timestamp_ms)

    @property
    def current_timestamp_ms__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def current_timestamp_ms__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_current_timestamp_ms(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_current_timestamp_ms)


    class Repeated_forts(RepeatedSequence):
        class pb_subtype(object):
            def __get__(self, instance, cls):
                return TYPE_FortData
        pb_subtype = pb_subtype()


    TYPE_Repeated_forts = Repeated_forts


    @property
    def forts__stream(self):
        if 3 in self._cache:
            def acc(v):
                v_ = lambda: v
                return v_
            return [acc(v) for v in self._cache[3]]
        return self._get_repeated(3, self.TYPE_Repeated_forts, "forts", lazy=True)

    def forts__fast_append(self, value):
        self._append_to_repeated(3, self.TYPE_Repeated_forts, value)

    def _get_forts(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, self.TYPE_Repeated_forts, 'forts')
            self._cache[3] = r
        return r

    def _establish_parentage_forts(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_forts), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_forts
                v._pbf_establish_parent_callback = self._establish_parentage_forts

    def _set_forts(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_forts(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field forts"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = self.TYPE_Repeated_forts

    def _mod_forts(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = self.TYPE_Repeated_forts

    def _del_forts(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "forts"

    forts = property(_get_forts, _set_forts, _del_forts)

    @property
    def forts__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def forts__type(self):
        return self.TYPE_Repeated_forts

    def _finalize_forts(cls):
        if is_string(cls.TYPE_Repeated_forts):
            cls._pbf_strings.append(3)
        elif _PB_type(cls.TYPE_Repeated_forts) is _PB_type:
            assert issubclass(cls.TYPE_Repeated_forts, RepeatedSequence)
            if is_string(cls.TYPE_Repeated_forts.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_forts)


    class Repeated_spawn_points(RepeatedSequence):
        class pb_subtype(object):
            def __get__(self, instance, cls):
                return TYPE_SpawnPoint
        pb_subtype = pb_subtype()


    TYPE_Repeated_spawn_points = Repeated_spawn_points


    @property
    def spawn_points__stream(self):
        if 4 in self._cache:
            def acc(v):
                v_ = lambda: v
                return v_
            return [acc(v) for v in self._cache[4]]
        return self._get_repeated(4, self.TYPE_Repeated_spawn_points, "spawn_points", lazy=True)

    def spawn_points__fast_append(self, value):
        self._append_to_repeated(4, self.TYPE_Repeated_spawn_points, value)

    def _get_spawn_points(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, self.TYPE_Repeated_spawn_points, 'spawn_points')
            self._cache[4] = r
        return r

    def _establish_parentage_spawn_points(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_spawn_points), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_spawn_points
                v._pbf_establish_parent_callback = self._establish_parentage_spawn_points

    def _set_spawn_points(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_spawn_points(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field spawn_points"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = self.TYPE_Repeated_spawn_points

    def _mod_spawn_points(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = self.TYPE_Repeated_spawn_points

    def _del_spawn_points(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "spawn_points"

    spawn_points = property(_get_spawn_points, _set_spawn_points, _del_spawn_points)

    @property
    def spawn_points__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def spawn_points__type(self):
        return self.TYPE_Repeated_spawn_points

    def _finalize_spawn_points(cls):
        if is_string(cls.TYPE_Repeated_spawn_points):
            cls._pbf_strings.append(4)
        elif _PB_type(cls.TYPE_Repeated_spawn_points) is _PB_type:
            assert issubclass(cls.TYPE_Repeated_spawn_points, RepeatedSequence)
            if is_string(cls.TYPE_Repeated_spawn_points.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_spawn_points)


    class Repeated_wild_pokemons(RepeatedSequence):
        class pb_subtype(object):
            def __get__(self, instance, cls):
                return TYPE_WildPokemon
        pb_subtype = pb_subtype()


    TYPE_Repeated_wild_pokemons = Repeated_wild_pokemons


    @property
    def wild_pokemons__stream(self):
        if 5 in self._cache:
            def acc(v):
                v_ = lambda: v
                return v_
            return [acc(v) for v in self._cache[5]]
        return self._get_repeated(5, self.TYPE_Repeated_wild_pokemons, "wild_pokemons", lazy=True)

    def wild_pokemons__fast_append(self, value):
        self._append_to_repeated(5, self.TYPE_Repeated_wild_pokemons, value)

    def _get_wild_pokemons(self):
        if 5 in self._cache:
            r = self._cache[5]
        else:
            r = self._buf_get(5, self.TYPE_Repeated_wild_pokemons, 'wild_pokemons')
            self._cache[5] = r
        return r

    def _establish_parentage_wild_pokemons(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_wild_pokemons), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_wild_pokemons
                v._pbf_establish_parent_callback = self._establish_parentage_wild_pokemons

    def _set_wild_pokemons(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_wild_pokemons(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field wild_pokemons"
            raise ProtoValueError(list_assign_error)
        self._cache[5] = v
        self._mods[5] = self.TYPE_Repeated_wild_pokemons

    def _mod_wild_pokemons(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[5] = self.TYPE_Repeated_wild_pokemons

    def _del_wild_pokemons(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 5 in self._cache:
            del self._cache[5]
        if 5 in self._mods:
            del self._mods[5]
        self._buf_del(5)

    _pb_field_name_5 = "wild_pokemons"

    wild_pokemons = property(_get_wild_pokemons, _set_wild_pokemons, _del_wild_pokemons)

    @property
    def wild_pokemons__exists(self):
        return 5 in self._mods or self._buf_exists(5)

    @property
    def wild_pokemons__type(self):
        return self.TYPE_Repeated_wild_pokemons

    def _finalize_wild_pokemons(cls):
        if is_string(cls.TYPE_Repeated_wild_pokemons):
            cls._pbf_strings.append(5)
        elif _PB_type(cls.TYPE_Repeated_wild_pokemons) is _PB_type:
            assert issubclass(cls.TYPE_Repeated_wild_pokemons, RepeatedSequence)
            if is_string(cls.TYPE_Repeated_wild_pokemons.pb_subtype):
                cls._pbf_strings.append(5)

    _pbf_finalizers.append(_finalize_wild_pokemons)


    class Repeated_deleted_objects(RepeatedSequence):
        class pb_subtype(object):
            def __get__(self, instance, cls):
                return ProtoBase.TYPE_string
        pb_subtype = pb_subtype()


    TYPE_Repeated_deleted_objects = Repeated_deleted_objects


    def _get_deleted_objects(self):
        if 6 in self._cache:
            r = self._cache[6]
        else:
            r = self._buf_get(6, self.TYPE_Repeated_deleted_objects, 'deleted_objects')
            self._cache[6] = r
        return r

    def _establish_parentage_deleted_objects(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_deleted_objects), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_deleted_objects
                v._pbf_establish_parent_callback = self._establish_parentage_deleted_objects

    def _set_deleted_objects(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_deleted_objects(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field deleted_objects"
            raise ProtoValueError(list_assign_error)
        self._cache[6] = v
        self._mods[6] = self.TYPE_Repeated_deleted_objects

    def _mod_deleted_objects(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[6] = self.TYPE_Repeated_deleted_objects

    def _del_deleted_objects(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 6 in self._cache:
            del self._cache[6]
        if 6 in self._mods:
            del self._mods[6]
        self._buf_del(6)

    _pb_field_name_6 = "deleted_objects"

    deleted_objects = property(_get_deleted_objects, _set_deleted_objects, _del_deleted_objects)

    @property
    def deleted_objects__exists(self):
        return 6 in self._mods or self._buf_exists(6)

    @property
    def deleted_objects__type(self):
        return self.TYPE_Repeated_deleted_objects

    def _finalize_deleted_objects(cls):
        if is_string(cls.TYPE_Repeated_deleted_objects):
            cls._pbf_strings.append(6)
        elif _PB_type(cls.TYPE_Repeated_deleted_objects) is _PB_type:
            assert issubclass(cls.TYPE_Repeated_deleted_objects, RepeatedSequence)
            if is_string(cls.TYPE_Repeated_deleted_objects.pb_subtype):
                cls._pbf_strings.append(6)

    _pbf_finalizers.append(_finalize_deleted_objects)


    def _get_is_truncated_list(self):
        if 7 in self._cache:
            r = self._cache[7]
        else:
            r = self._buf_get(7, ProtoBase.TYPE_bool, 'is_truncated_list')
            self._cache[7] = r
        return r

    def _establish_parentage_is_truncated_list(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_is_truncated_list), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_is_truncated_list
                v._pbf_establish_parent_callback = self._establish_parentage_is_truncated_list

    def _set_is_truncated_list(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_is_truncated_list(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field is_truncated_list"
            raise ProtoValueError(list_assign_error)
        self._cache[7] = v
        self._mods[7] = ProtoBase.TYPE_bool

    def _mod_is_truncated_list(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[7] = ProtoBase.TYPE_bool

    def _del_is_truncated_list(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 7 in self._cache:
            del self._cache[7]
        if 7 in self._mods:
            del self._mods[7]
        self._buf_del(7)

    _pb_field_name_7 = "is_truncated_list"

    is_truncated_list = property(_get_is_truncated_list, _set_is_truncated_list, _del_is_truncated_list)

    @property
    def is_truncated_list__exists(self):
        return 7 in self._mods or self._buf_exists(7)

    @property
    def is_truncated_list__type(self):
        return ProtoBase.TYPE_bool

    def _finalize_is_truncated_list(cls):
        if is_string(ProtoBase.TYPE_bool):
            cls._pbf_strings.append(7)
        elif _PB_type(ProtoBase.TYPE_bool) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bool, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bool.pb_subtype):
                cls._pbf_strings.append(7)

    _pbf_finalizers.append(_finalize_is_truncated_list)


    class Repeated_fort_summaries(RepeatedSequence):
        class pb_subtype(object):
            def __get__(self, instance, cls):
                return TYPE_FortSummary
        pb_subtype = pb_subtype()


    TYPE_Repeated_fort_summaries = Repeated_fort_summaries


    @property
    def fort_summaries__stream(self):
        if 8 in self._cache:
            def acc(v):
                v_ = lambda: v
                return v_
            return [acc(v) for v in self._cache[8]]
        return self._get_repeated(8, self.TYPE_Repeated_fort_summaries, "fort_summaries", lazy=True)

    def fort_summaries__fast_append(self, value):
        self._append_to_repeated(8, self.TYPE_Repeated_fort_summaries, value)

    def _get_fort_summaries(self):
        if 8 in self._cache:
            r = self._cache[8]
        else:
            r = self._buf_get(8, self.TYPE_Repeated_fort_summaries, 'fort_summaries')
            self._cache[8] = r
        return r

    def _establish_parentage_fort_summaries(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_fort_summaries), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_fort_summaries
                v._pbf_establish_parent_callback = self._establish_parentage_fort_summaries

    def _set_fort_summaries(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_fort_summaries(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field fort_summaries"
            raise ProtoValueError(list_assign_error)
        self._cache[8] = v
        self._mods[8] = self.TYPE_Repeated_fort_summaries

    def _mod_fort_summaries(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[8] = self.TYPE_Repeated_fort_summaries

    def _del_fort_summaries(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 8 in self._cache:
            del self._cache[8]
        if 8 in self._mods:
            del self._mods[8]
        self._buf_del(8)

    _pb_field_name_8 = "fort_summaries"

    fort_summaries = property(_get_fort_summaries, _set_fort_summaries, _del_fort_summaries)

    @property
    def fort_summaries__exists(self):
        return 8 in self._mods or self._buf_exists(8)

    @property
    def fort_summaries__type(self):
        return self.TYPE_Repeated_fort_summaries

    def _finalize_fort_summaries(cls):
        if is_string(cls.TYPE_Repeated_fort_summaries):
            cls._pbf_strings.append(8)
        elif _PB_type(cls.TYPE_Repeated_fort_summaries) is _PB_type:
            assert issubclass(cls.TYPE_Repeated_fort_summaries, RepeatedSequence)
            if is_string(cls.TYPE_Repeated_fort_summaries.pb_subtype):
                cls._pbf_strings.append(8)

    _pbf_finalizers.append(_finalize_fort_summaries)


    class Repeated_decimated_spawn_points(RepeatedSequence):
        class pb_subtype(object):
            def __get__(self, instance, cls):
                return TYPE_SpawnPoint
        pb_subtype = pb_subtype()


    TYPE_Repeated_decimated_spawn_points = Repeated_decimated_spawn_points


    @property
    def decimated_spawn_points__stream(self):
        if 9 in self._cache:
            def acc(v):
                v_ = lambda: v
                return v_
            return [acc(v) for v in self._cache[9]]
        return self._get_repeated(9, self.TYPE_Repeated_decimated_spawn_points, "decimated_spawn_points", lazy=True)

    def decimated_spawn_points__fast_append(self, value):
        self._append_to_repeated(9, self.TYPE_Repeated_decimated_spawn_points, value)

    def _get_decimated_spawn_points(self):
        if 9 in self._cache:
            r = self._cache[9]
        else:
            r = self._buf_get(9, self.TYPE_Repeated_decimated_spawn_points, 'decimated_spawn_points')
            self._cache[9] = r
        return r

    def _establish_parentage_decimated_spawn_points(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_decimated_spawn_points), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_decimated_spawn_points
                v._pbf_establish_parent_callback = self._establish_parentage_decimated_spawn_points

    def _set_decimated_spawn_points(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_decimated_spawn_points(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field decimated_spawn_points"
            raise ProtoValueError(list_assign_error)
        self._cache[9] = v
        self._mods[9] = self.TYPE_Repeated_decimated_spawn_points

    def _mod_decimated_spawn_points(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[9] = self.TYPE_Repeated_decimated_spawn_points

    def _del_decimated_spawn_points(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 9 in self._cache:
            del self._cache[9]
        if 9 in self._mods:
            del self._mods[9]
        self._buf_del(9)

    _pb_field_name_9 = "decimated_spawn_points"

    decimated_spawn_points = property(_get_decimated_spawn_points, _set_decimated_spawn_points, _del_decimated_spawn_points)

    @property
    def decimated_spawn_points__exists(self):
        return 9 in self._mods or self._buf_exists(9)

    @property
    def decimated_spawn_points__type(self):
        return self.TYPE_Repeated_decimated_spawn_points

    def _finalize_decimated_spawn_points(cls):
        if is_string(cls.TYPE_Repeated_decimated_spawn_points):
            cls._pbf_strings.append(9)
        elif _PB_type(cls.TYPE_Repeated_decimated_spawn_points) is _PB_type:
            assert issubclass(cls.TYPE_Repeated_decimated_spawn_points, RepeatedSequence)
            if is_string(cls.TYPE_Repeated_decimated_spawn_points.pb_subtype):
                cls._pbf_strings.append(9)

    _pbf_finalizers.append(_finalize_decimated_spawn_points)


    class Repeated_catchable_pokemons(RepeatedSequence):
        class pb_subtype(object):
            def __get__(self, instance, cls):
                return TYPE_MapPokemon
        pb_subtype = pb_subtype()


    TYPE_Repeated_catchable_pokemons = Repeated_catchable_pokemons


    @property
    def catchable_pokemons__stream(self):
        if 10 in self._cache:
            def acc(v):
                v_ = lambda: v
                return v_
            return [acc(v) for v in self._cache[10]]
        return self._get_repeated(10, self.TYPE_Repeated_catchable_pokemons, "catchable_pokemons", lazy=True)

    def catchable_pokemons__fast_append(self, value):
        self._append_to_repeated(10, self.TYPE_Repeated_catchable_pokemons, value)

    def _get_catchable_pokemons(self):
        if 10 in self._cache:
            r = self._cache[10]
        else:
            r = self._buf_get(10, self.TYPE_Repeated_catchable_pokemons, 'catchable_pokemons')
            self._cache[10] = r
        return r

    def _establish_parentage_catchable_pokemons(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_catchable_pokemons), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_catchable_pokemons
                v._pbf_establish_parent_callback = self._establish_parentage_catchable_pokemons

    def _set_catchable_pokemons(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_catchable_pokemons(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field catchable_pokemons"
            raise ProtoValueError(list_assign_error)
        self._cache[10] = v
        self._mods[10] = self.TYPE_Repeated_catchable_pokemons

    def _mod_catchable_pokemons(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[10] = self.TYPE_Repeated_catchable_pokemons

    def _del_catchable_pokemons(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 10 in self._cache:
            del self._cache[10]
        if 10 in self._mods:
            del self._mods[10]
        self._buf_del(10)

    _pb_field_name_10 = "catchable_pokemons"

    catchable_pokemons = property(_get_catchable_pokemons, _set_catchable_pokemons, _del_catchable_pokemons)

    @property
    def catchable_pokemons__exists(self):
        return 10 in self._mods or self._buf_exists(10)

    @property
    def catchable_pokemons__type(self):
        return self.TYPE_Repeated_catchable_pokemons

    def _finalize_catchable_pokemons(cls):
        if is_string(cls.TYPE_Repeated_catchable_pokemons):
            cls._pbf_strings.append(10)
        elif _PB_type(cls.TYPE_Repeated_catchable_pokemons) is _PB_type:
            assert issubclass(cls.TYPE_Repeated_catchable_pokemons, RepeatedSequence)
            if is_string(cls.TYPE_Repeated_catchable_pokemons.pb_subtype):
                cls._pbf_strings.append(10)

    _pbf_finalizers.append(_finalize_catchable_pokemons)


    class Repeated_nearby_pokemons(RepeatedSequence):
        class pb_subtype(object):
            def __get__(self, instance, cls):
                return TYPE_NearbyPokemon
        pb_subtype = pb_subtype()


    TYPE_Repeated_nearby_pokemons = Repeated_nearby_pokemons


    @property
    def nearby_pokemons__stream(self):
        if 11 in self._cache:
            def acc(v):
                v_ = lambda: v
                return v_
            return [acc(v) for v in self._cache[11]]
        return self._get_repeated(11, self.TYPE_Repeated_nearby_pokemons, "nearby_pokemons", lazy=True)

    def nearby_pokemons__fast_append(self, value):
        self._append_to_repeated(11, self.TYPE_Repeated_nearby_pokemons, value)

    def _get_nearby_pokemons(self):
        if 11 in self._cache:
            r = self._cache[11]
        else:
            r = self._buf_get(11, self.TYPE_Repeated_nearby_pokemons, 'nearby_pokemons')
            self._cache[11] = r
        return r

    def _establish_parentage_nearby_pokemons(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_nearby_pokemons), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_nearby_pokemons
                v._pbf_establish_parent_callback = self._establish_parentage_nearby_pokemons

    def _set_nearby_pokemons(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_nearby_pokemons(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field nearby_pokemons"
            raise ProtoValueError(list_assign_error)
        self._cache[11] = v
        self._mods[11] = self.TYPE_Repeated_nearby_pokemons

    def _mod_nearby_pokemons(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[11] = self.TYPE_Repeated_nearby_pokemons

    def _del_nearby_pokemons(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 11 in self._cache:
            del self._cache[11]
        if 11 in self._mods:
            del self._mods[11]
        self._buf_del(11)

    _pb_field_name_11 = "nearby_pokemons"

    nearby_pokemons = property(_get_nearby_pokemons, _set_nearby_pokemons, _del_nearby_pokemons)

    @property
    def nearby_pokemons__exists(self):
        return 11 in self._mods or self._buf_exists(11)

    @property
    def nearby_pokemons__type(self):
        return self.TYPE_Repeated_nearby_pokemons

    def _finalize_nearby_pokemons(cls):
        if is_string(cls.TYPE_Repeated_nearby_pokemons):
            cls._pbf_strings.append(11)
        elif _PB_type(cls.TYPE_Repeated_nearby_pokemons) is _PB_type:
            assert issubclass(cls.TYPE_Repeated_nearby_pokemons, RepeatedSequence)
            if is_string(cls.TYPE_Repeated_nearby_pokemons.pb_subtype):
                cls._pbf_strings.append(11)

    _pbf_finalizers.append(_finalize_nearby_pokemons)


TYPE_MapCell = MapCell
_PB_finalizers.append('MapCell')

class FortData(ProtoBase):
    _required = []
    _field_map = {'rendering_type': 16, 'gym_points': 10, 'is_in_battle': 11, 'last_modified_timestamp_ms': 2, 'guard_pokemon_id': 6, 'enabled': 8, 'longitude': 4, 'guard_pokemon_cp': 7, 'lure_info': 13, 'cooldown_complete_timestamp_ms': 14, 'sponsor': 15, 'active_fort_modifier': 12, 'latitude': 3, 'owned_by_team': 5, 'type': 9, 'id': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['id', 'last_modified_timestamp_ms', 'latitude', 'longitude', 'owned_by_team', 'guard_pokemon_id', 'guard_pokemon_cp', 'enabled', 'type', 'gym_points', 'is_in_battle', 'active_fort_modifier', 'lure_info', 'cooldown_complete_timestamp_ms', 'sponsor', 'rendering_type']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_id(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_string, 'id')
            self._cache[1] = r
        return r

    def _establish_parentage_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_id
                v._pbf_establish_parent_callback = self._establish_parentage_id

    def _set_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field id"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_string

    def _mod_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_string

    def _del_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "id"

    id = property(_get_id, _set_id, _del_id)

    @property
    def id__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def id__type(self):
        return ProtoBase.TYPE_string

    def _finalize_id(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_id)


    def _get_last_modified_timestamp_ms(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int64, 'last_modified_timestamp_ms')
            self._cache[2] = r
        return r

    def _establish_parentage_last_modified_timestamp_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_last_modified_timestamp_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_last_modified_timestamp_ms
                v._pbf_establish_parent_callback = self._establish_parentage_last_modified_timestamp_ms

    def _set_last_modified_timestamp_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_last_modified_timestamp_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field last_modified_timestamp_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_int64

    def _mod_last_modified_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int64

    def _del_last_modified_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "last_modified_timestamp_ms"

    last_modified_timestamp_ms = property(_get_last_modified_timestamp_ms, _set_last_modified_timestamp_ms, _del_last_modified_timestamp_ms)

    @property
    def last_modified_timestamp_ms__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def last_modified_timestamp_ms__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_last_modified_timestamp_ms(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_last_modified_timestamp_ms)


    def _get_latitude(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_double, 'latitude')
            self._cache[3] = r
        return r

    def _establish_parentage_latitude(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_latitude), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_latitude
                v._pbf_establish_parent_callback = self._establish_parentage_latitude

    def _set_latitude(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_latitude(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field latitude"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_double

    def _mod_latitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_double

    def _del_latitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "latitude"

    latitude = property(_get_latitude, _set_latitude, _del_latitude)

    @property
    def latitude__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def latitude__type(self):
        return ProtoBase.TYPE_double

    def _finalize_latitude(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_latitude)


    def _get_longitude(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, ProtoBase.TYPE_double, 'longitude')
            self._cache[4] = r
        return r

    def _establish_parentage_longitude(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_longitude), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_longitude
                v._pbf_establish_parent_callback = self._establish_parentage_longitude

    def _set_longitude(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_longitude(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field longitude"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = ProtoBase.TYPE_double

    def _mod_longitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = ProtoBase.TYPE_double

    def _del_longitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "longitude"

    longitude = property(_get_longitude, _set_longitude, _del_longitude)

    @property
    def longitude__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def longitude__type(self):
        return ProtoBase.TYPE_double

    def _finalize_longitude(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(4)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_longitude)


    def _get_owned_by_team(self):
        if 5 in self._cache:
            r = self._cache[5]
        else:
            r = self._buf_get(5, RpcEnum_palm.TYPE_TeamColor, 'owned_by_team')
            self._cache[5] = r
        return r

    def _establish_parentage_owned_by_team(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_owned_by_team), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_owned_by_team
                v._pbf_establish_parent_callback = self._establish_parentage_owned_by_team

    def _set_owned_by_team(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_owned_by_team(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field owned_by_team"
            raise ProtoValueError(list_assign_error)
        self._cache[5] = v
        self._mods[5] = RpcEnum_palm.TYPE_TeamColor

    def _mod_owned_by_team(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[5] = RpcEnum_palm.TYPE_TeamColor

    def _del_owned_by_team(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 5 in self._cache:
            del self._cache[5]
        if 5 in self._mods:
            del self._mods[5]
        self._buf_del(5)

    _pb_field_name_5 = "owned_by_team"

    owned_by_team = property(_get_owned_by_team, _set_owned_by_team, _del_owned_by_team)

    @property
    def owned_by_team__exists(self):
        return 5 in self._mods or self._buf_exists(5)

    @property
    def owned_by_team__type(self):
        return RpcEnum_palm.TYPE_TeamColor

    def _finalize_owned_by_team(cls):
        if is_string(RpcEnum_palm.TYPE_TeamColor):
            cls._pbf_strings.append(5)
        elif _PB_type(RpcEnum_palm.TYPE_TeamColor) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_TeamColor, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_TeamColor.pb_subtype):
                cls._pbf_strings.append(5)

    _pbf_finalizers.append(_finalize_owned_by_team)


    def _get_guard_pokemon_id(self):
        if 6 in self._cache:
            r = self._cache[6]
        else:
            r = self._buf_get(6, RpcEnum_palm.TYPE_PokemonId, 'guard_pokemon_id')
            self._cache[6] = r
        return r

    def _establish_parentage_guard_pokemon_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_guard_pokemon_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_guard_pokemon_id
                v._pbf_establish_parent_callback = self._establish_parentage_guard_pokemon_id

    def _set_guard_pokemon_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_guard_pokemon_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field guard_pokemon_id"
            raise ProtoValueError(list_assign_error)
        self._cache[6] = v
        self._mods[6] = RpcEnum_palm.TYPE_PokemonId

    def _mod_guard_pokemon_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[6] = RpcEnum_palm.TYPE_PokemonId

    def _del_guard_pokemon_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 6 in self._cache:
            del self._cache[6]
        if 6 in self._mods:
            del self._mods[6]
        self._buf_del(6)

    _pb_field_name_6 = "guard_pokemon_id"

    guard_pokemon_id = property(_get_guard_pokemon_id, _set_guard_pokemon_id, _del_guard_pokemon_id)

    @property
    def guard_pokemon_id__exists(self):
        return 6 in self._mods or self._buf_exists(6)

    @property
    def guard_pokemon_id__type(self):
        return RpcEnum_palm.TYPE_PokemonId

    def _finalize_guard_pokemon_id(cls):
        if is_string(RpcEnum_palm.TYPE_PokemonId):
            cls._pbf_strings.append(6)
        elif _PB_type(RpcEnum_palm.TYPE_PokemonId) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_PokemonId, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_PokemonId.pb_subtype):
                cls._pbf_strings.append(6)

    _pbf_finalizers.append(_finalize_guard_pokemon_id)


    def _get_guard_pokemon_cp(self):
        if 7 in self._cache:
            r = self._cache[7]
        else:
            r = self._buf_get(7, ProtoBase.TYPE_int32, 'guard_pokemon_cp')
            self._cache[7] = r
        return r

    def _establish_parentage_guard_pokemon_cp(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_guard_pokemon_cp), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_guard_pokemon_cp
                v._pbf_establish_parent_callback = self._establish_parentage_guard_pokemon_cp

    def _set_guard_pokemon_cp(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_guard_pokemon_cp(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field guard_pokemon_cp"
            raise ProtoValueError(list_assign_error)
        self._cache[7] = v
        self._mods[7] = ProtoBase.TYPE_int32

    def _mod_guard_pokemon_cp(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[7] = ProtoBase.TYPE_int32

    def _del_guard_pokemon_cp(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 7 in self._cache:
            del self._cache[7]
        if 7 in self._mods:
            del self._mods[7]
        self._buf_del(7)

    _pb_field_name_7 = "guard_pokemon_cp"

    guard_pokemon_cp = property(_get_guard_pokemon_cp, _set_guard_pokemon_cp, _del_guard_pokemon_cp)

    @property
    def guard_pokemon_cp__exists(self):
        return 7 in self._mods or self._buf_exists(7)

    @property
    def guard_pokemon_cp__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_guard_pokemon_cp(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(7)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(7)

    _pbf_finalizers.append(_finalize_guard_pokemon_cp)


    def _get_enabled(self):
        if 8 in self._cache:
            r = self._cache[8]
        else:
            r = self._buf_get(8, ProtoBase.TYPE_bool, 'enabled')
            self._cache[8] = r
        return r

    def _establish_parentage_enabled(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_enabled), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_enabled
                v._pbf_establish_parent_callback = self._establish_parentage_enabled

    def _set_enabled(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_enabled(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field enabled"
            raise ProtoValueError(list_assign_error)
        self._cache[8] = v
        self._mods[8] = ProtoBase.TYPE_bool

    def _mod_enabled(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[8] = ProtoBase.TYPE_bool

    def _del_enabled(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 8 in self._cache:
            del self._cache[8]
        if 8 in self._mods:
            del self._mods[8]
        self._buf_del(8)

    _pb_field_name_8 = "enabled"

    enabled = property(_get_enabled, _set_enabled, _del_enabled)

    @property
    def enabled__exists(self):
        return 8 in self._mods or self._buf_exists(8)

    @property
    def enabled__type(self):
        return ProtoBase.TYPE_bool

    def _finalize_enabled(cls):
        if is_string(ProtoBase.TYPE_bool):
            cls._pbf_strings.append(8)
        elif _PB_type(ProtoBase.TYPE_bool) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bool, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bool.pb_subtype):
                cls._pbf_strings.append(8)

    _pbf_finalizers.append(_finalize_enabled)


    def _get_type(self):
        if 9 in self._cache:
            r = self._cache[9]
        else:
            r = self._buf_get(9, RpcEnum_palm.TYPE_FortType, 'type')
            self._cache[9] = r
        return r

    def _establish_parentage_type(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_type), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_type
                v._pbf_establish_parent_callback = self._establish_parentage_type

    def _set_type(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_type(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field type"
            raise ProtoValueError(list_assign_error)
        self._cache[9] = v
        self._mods[9] = RpcEnum_palm.TYPE_FortType

    def _mod_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[9] = RpcEnum_palm.TYPE_FortType

    def _del_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 9 in self._cache:
            del self._cache[9]
        if 9 in self._mods:
            del self._mods[9]
        self._buf_del(9)

    _pb_field_name_9 = "type"

    type = property(_get_type, _set_type, _del_type)

    @property
    def type__exists(self):
        return 9 in self._mods or self._buf_exists(9)

    @property
    def type__type(self):
        return RpcEnum_palm.TYPE_FortType

    def _finalize_type(cls):
        if is_string(RpcEnum_palm.TYPE_FortType):
            cls._pbf_strings.append(9)
        elif _PB_type(RpcEnum_palm.TYPE_FortType) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_FortType, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_FortType.pb_subtype):
                cls._pbf_strings.append(9)

    _pbf_finalizers.append(_finalize_type)


    def _get_gym_points(self):
        if 10 in self._cache:
            r = self._cache[10]
        else:
            r = self._buf_get(10, ProtoBase.TYPE_int64, 'gym_points')
            self._cache[10] = r
        return r

    def _establish_parentage_gym_points(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_gym_points), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_gym_points
                v._pbf_establish_parent_callback = self._establish_parentage_gym_points

    def _set_gym_points(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_gym_points(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field gym_points"
            raise ProtoValueError(list_assign_error)
        self._cache[10] = v
        self._mods[10] = ProtoBase.TYPE_int64

    def _mod_gym_points(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[10] = ProtoBase.TYPE_int64

    def _del_gym_points(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 10 in self._cache:
            del self._cache[10]
        if 10 in self._mods:
            del self._mods[10]
        self._buf_del(10)

    _pb_field_name_10 = "gym_points"

    gym_points = property(_get_gym_points, _set_gym_points, _del_gym_points)

    @property
    def gym_points__exists(self):
        return 10 in self._mods or self._buf_exists(10)

    @property
    def gym_points__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_gym_points(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(10)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(10)

    _pbf_finalizers.append(_finalize_gym_points)


    def _get_is_in_battle(self):
        if 11 in self._cache:
            r = self._cache[11]
        else:
            r = self._buf_get(11, ProtoBase.TYPE_bool, 'is_in_battle')
            self._cache[11] = r
        return r

    def _establish_parentage_is_in_battle(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_is_in_battle), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_is_in_battle
                v._pbf_establish_parent_callback = self._establish_parentage_is_in_battle

    def _set_is_in_battle(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_is_in_battle(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field is_in_battle"
            raise ProtoValueError(list_assign_error)
        self._cache[11] = v
        self._mods[11] = ProtoBase.TYPE_bool

    def _mod_is_in_battle(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[11] = ProtoBase.TYPE_bool

    def _del_is_in_battle(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 11 in self._cache:
            del self._cache[11]
        if 11 in self._mods:
            del self._mods[11]
        self._buf_del(11)

    _pb_field_name_11 = "is_in_battle"

    is_in_battle = property(_get_is_in_battle, _set_is_in_battle, _del_is_in_battle)

    @property
    def is_in_battle__exists(self):
        return 11 in self._mods or self._buf_exists(11)

    @property
    def is_in_battle__type(self):
        return ProtoBase.TYPE_bool

    def _finalize_is_in_battle(cls):
        if is_string(ProtoBase.TYPE_bool):
            cls._pbf_strings.append(11)
        elif _PB_type(ProtoBase.TYPE_bool) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bool, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bool.pb_subtype):
                cls._pbf_strings.append(11)

    _pbf_finalizers.append(_finalize_is_in_battle)


    def _get_active_fort_modifier(self):
        if 12 in self._cache:
            r = self._cache[12]
        else:
            r = self._buf_get(12, ProtoBase.TYPE_bytes, 'active_fort_modifier')
            self._cache[12] = r
        return r

    def _establish_parentage_active_fort_modifier(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_active_fort_modifier), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_active_fort_modifier
                v._pbf_establish_parent_callback = self._establish_parentage_active_fort_modifier

    def _set_active_fort_modifier(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_active_fort_modifier(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field active_fort_modifier"
            raise ProtoValueError(list_assign_error)
        self._cache[12] = v
        self._mods[12] = ProtoBase.TYPE_bytes

    def _mod_active_fort_modifier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[12] = ProtoBase.TYPE_bytes

    def _del_active_fort_modifier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 12 in self._cache:
            del self._cache[12]
        if 12 in self._mods:
            del self._mods[12]
        self._buf_del(12)

    _pb_field_name_12 = "active_fort_modifier"

    active_fort_modifier = property(_get_active_fort_modifier, _set_active_fort_modifier, _del_active_fort_modifier)

    @property
    def active_fort_modifier__exists(self):
        return 12 in self._mods or self._buf_exists(12)

    @property
    def active_fort_modifier__type(self):
        return ProtoBase.TYPE_bytes

    def _finalize_active_fort_modifier(cls):
        if is_string(ProtoBase.TYPE_bytes):
            cls._pbf_strings.append(12)
        elif _PB_type(ProtoBase.TYPE_bytes) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bytes, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bytes.pb_subtype):
                cls._pbf_strings.append(12)

    _pbf_finalizers.append(_finalize_active_fort_modifier)


    def _get_lure_info(self):
        if 13 in self._cache:
            r = self._cache[13]
        else:
            r = self._buf_get(13, TYPE_FortLureInfo, 'lure_info')
            self._cache[13] = r
        return r

    def _establish_parentage_lure_info(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_lure_info), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_lure_info
                v._pbf_establish_parent_callback = self._establish_parentage_lure_info

    def _set_lure_info(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_lure_info(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field lure_info"
            raise ProtoValueError(list_assign_error)
        self._cache[13] = v
        self._mods[13] = TYPE_FortLureInfo

    def _mod_lure_info(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[13] = TYPE_FortLureInfo

    def _del_lure_info(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 13 in self._cache:
            del self._cache[13]
        if 13 in self._mods:
            del self._mods[13]
        self._buf_del(13)

    _pb_field_name_13 = "lure_info"

    lure_info = property(_get_lure_info, _set_lure_info, _del_lure_info)

    @property
    def lure_info__exists(self):
        return 13 in self._mods or self._buf_exists(13)

    @property
    def lure_info__type(self):
        return TYPE_FortLureInfo

    def _finalize_lure_info(cls):
        if is_string(TYPE_FortLureInfo):
            cls._pbf_strings.append(13)
        elif _PB_type(TYPE_FortLureInfo) is _PB_type:
            assert issubclass(TYPE_FortLureInfo, RepeatedSequence)
            if is_string(TYPE_FortLureInfo.pb_subtype):
                cls._pbf_strings.append(13)

    _pbf_finalizers.append(_finalize_lure_info)


    def _get_cooldown_complete_timestamp_ms(self):
        if 14 in self._cache:
            r = self._cache[14]
        else:
            r = self._buf_get(14, ProtoBase.TYPE_int64, 'cooldown_complete_timestamp_ms')
            self._cache[14] = r
        return r

    def _establish_parentage_cooldown_complete_timestamp_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_cooldown_complete_timestamp_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_cooldown_complete_timestamp_ms
                v._pbf_establish_parent_callback = self._establish_parentage_cooldown_complete_timestamp_ms

    def _set_cooldown_complete_timestamp_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_cooldown_complete_timestamp_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field cooldown_complete_timestamp_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[14] = v
        self._mods[14] = ProtoBase.TYPE_int64

    def _mod_cooldown_complete_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[14] = ProtoBase.TYPE_int64

    def _del_cooldown_complete_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 14 in self._cache:
            del self._cache[14]
        if 14 in self._mods:
            del self._mods[14]
        self._buf_del(14)

    _pb_field_name_14 = "cooldown_complete_timestamp_ms"

    cooldown_complete_timestamp_ms = property(_get_cooldown_complete_timestamp_ms, _set_cooldown_complete_timestamp_ms, _del_cooldown_complete_timestamp_ms)

    @property
    def cooldown_complete_timestamp_ms__exists(self):
        return 14 in self._mods or self._buf_exists(14)

    @property
    def cooldown_complete_timestamp_ms__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_cooldown_complete_timestamp_ms(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(14)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(14)

    _pbf_finalizers.append(_finalize_cooldown_complete_timestamp_ms)


    def _get_sponsor(self):
        if 15 in self._cache:
            r = self._cache[15]
        else:
            r = self._buf_get(15, RpcEnum_palm.TYPE_FortSponsor, 'sponsor')
            self._cache[15] = r
        return r

    def _establish_parentage_sponsor(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_sponsor), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_sponsor
                v._pbf_establish_parent_callback = self._establish_parentage_sponsor

    def _set_sponsor(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_sponsor(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field sponsor"
            raise ProtoValueError(list_assign_error)
        self._cache[15] = v
        self._mods[15] = RpcEnum_palm.TYPE_FortSponsor

    def _mod_sponsor(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[15] = RpcEnum_palm.TYPE_FortSponsor

    def _del_sponsor(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 15 in self._cache:
            del self._cache[15]
        if 15 in self._mods:
            del self._mods[15]
        self._buf_del(15)

    _pb_field_name_15 = "sponsor"

    sponsor = property(_get_sponsor, _set_sponsor, _del_sponsor)

    @property
    def sponsor__exists(self):
        return 15 in self._mods or self._buf_exists(15)

    @property
    def sponsor__type(self):
        return RpcEnum_palm.TYPE_FortSponsor

    def _finalize_sponsor(cls):
        if is_string(RpcEnum_palm.TYPE_FortSponsor):
            cls._pbf_strings.append(15)
        elif _PB_type(RpcEnum_palm.TYPE_FortSponsor) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_FortSponsor, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_FortSponsor.pb_subtype):
                cls._pbf_strings.append(15)

    _pbf_finalizers.append(_finalize_sponsor)


    def _get_rendering_type(self):
        if 16 in self._cache:
            r = self._cache[16]
        else:
            r = self._buf_get(16, RpcEnum_palm.TYPE_FortRenderingType, 'rendering_type')
            self._cache[16] = r
        return r

    def _establish_parentage_rendering_type(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_rendering_type), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_rendering_type
                v._pbf_establish_parent_callback = self._establish_parentage_rendering_type

    def _set_rendering_type(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_rendering_type(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field rendering_type"
            raise ProtoValueError(list_assign_error)
        self._cache[16] = v
        self._mods[16] = RpcEnum_palm.TYPE_FortRenderingType

    def _mod_rendering_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[16] = RpcEnum_palm.TYPE_FortRenderingType

    def _del_rendering_type(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 16 in self._cache:
            del self._cache[16]
        if 16 in self._mods:
            del self._mods[16]
        self._buf_del(16)

    _pb_field_name_16 = "rendering_type"

    rendering_type = property(_get_rendering_type, _set_rendering_type, _del_rendering_type)

    @property
    def rendering_type__exists(self):
        return 16 in self._mods or self._buf_exists(16)

    @property
    def rendering_type__type(self):
        return RpcEnum_palm.TYPE_FortRenderingType

    def _finalize_rendering_type(cls):
        if is_string(RpcEnum_palm.TYPE_FortRenderingType):
            cls._pbf_strings.append(16)
        elif _PB_type(RpcEnum_palm.TYPE_FortRenderingType) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_FortRenderingType, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_FortRenderingType.pb_subtype):
                cls._pbf_strings.append(16)

    _pbf_finalizers.append(_finalize_rendering_type)


TYPE_FortData = FortData
_PB_finalizers.append('FortData')

class FortLureInfo(ProtoBase):
    _required = []
    _field_map = {'unknown2': 2, 'fort_id': 1, 'lure_expires_timestamp_ms': 4, 'active_pokemon_id': 3}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['fort_id', 'unknown2', 'active_pokemon_id', 'lure_expires_timestamp_ms']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_fort_id(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_string, 'fort_id')
            self._cache[1] = r
        return r

    def _establish_parentage_fort_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_fort_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_fort_id
                v._pbf_establish_parent_callback = self._establish_parentage_fort_id

    def _set_fort_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_fort_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field fort_id"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_string

    def _mod_fort_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_string

    def _del_fort_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "fort_id"

    fort_id = property(_get_fort_id, _set_fort_id, _del_fort_id)

    @property
    def fort_id__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def fort_id__type(self):
        return ProtoBase.TYPE_string

    def _finalize_fort_id(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_fort_id)


    def _get_unknown2(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_double, 'unknown2')
            self._cache[2] = r
        return r

    def _establish_parentage_unknown2(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_unknown2), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_unknown2
                v._pbf_establish_parent_callback = self._establish_parentage_unknown2

    def _set_unknown2(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_unknown2(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field unknown2"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_double

    def _mod_unknown2(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_double

    def _del_unknown2(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "unknown2"

    unknown2 = property(_get_unknown2, _set_unknown2, _del_unknown2)

    @property
    def unknown2__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def unknown2__type(self):
        return ProtoBase.TYPE_double

    def _finalize_unknown2(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_unknown2)


    def _get_active_pokemon_id(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, RpcEnum_palm.TYPE_PokemonId, 'active_pokemon_id')
            self._cache[3] = r
        return r

    def _establish_parentage_active_pokemon_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_active_pokemon_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_active_pokemon_id
                v._pbf_establish_parent_callback = self._establish_parentage_active_pokemon_id

    def _set_active_pokemon_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_active_pokemon_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field active_pokemon_id"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = RpcEnum_palm.TYPE_PokemonId

    def _mod_active_pokemon_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = RpcEnum_palm.TYPE_PokemonId

    def _del_active_pokemon_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "active_pokemon_id"

    active_pokemon_id = property(_get_active_pokemon_id, _set_active_pokemon_id, _del_active_pokemon_id)

    @property
    def active_pokemon_id__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def active_pokemon_id__type(self):
        return RpcEnum_palm.TYPE_PokemonId

    def _finalize_active_pokemon_id(cls):
        if is_string(RpcEnum_palm.TYPE_PokemonId):
            cls._pbf_strings.append(3)
        elif _PB_type(RpcEnum_palm.TYPE_PokemonId) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_PokemonId, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_PokemonId.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_active_pokemon_id)


    def _get_lure_expires_timestamp_ms(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, ProtoBase.TYPE_int64, 'lure_expires_timestamp_ms')
            self._cache[4] = r
        return r

    def _establish_parentage_lure_expires_timestamp_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_lure_expires_timestamp_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_lure_expires_timestamp_ms
                v._pbf_establish_parent_callback = self._establish_parentage_lure_expires_timestamp_ms

    def _set_lure_expires_timestamp_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_lure_expires_timestamp_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field lure_expires_timestamp_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = ProtoBase.TYPE_int64

    def _mod_lure_expires_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = ProtoBase.TYPE_int64

    def _del_lure_expires_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "lure_expires_timestamp_ms"

    lure_expires_timestamp_ms = property(_get_lure_expires_timestamp_ms, _set_lure_expires_timestamp_ms, _del_lure_expires_timestamp_ms)

    @property
    def lure_expires_timestamp_ms__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def lure_expires_timestamp_ms__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_lure_expires_timestamp_ms(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(4)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_lure_expires_timestamp_ms)


TYPE_FortLureInfo = FortLureInfo
_PB_finalizers.append('FortLureInfo')

class SpawnPoint(ProtoBase):
    _required = []
    _field_map = {'latitude': 2, 'longitude': 3}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['latitude', 'longitude']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_latitude(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_double, 'latitude')
            self._cache[2] = r
        return r

    def _establish_parentage_latitude(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_latitude), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_latitude
                v._pbf_establish_parent_callback = self._establish_parentage_latitude

    def _set_latitude(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_latitude(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field latitude"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_double

    def _mod_latitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_double

    def _del_latitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "latitude"

    latitude = property(_get_latitude, _set_latitude, _del_latitude)

    @property
    def latitude__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def latitude__type(self):
        return ProtoBase.TYPE_double

    def _finalize_latitude(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_latitude)


    def _get_longitude(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_double, 'longitude')
            self._cache[3] = r
        return r

    def _establish_parentage_longitude(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_longitude), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_longitude
                v._pbf_establish_parent_callback = self._establish_parentage_longitude

    def _set_longitude(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_longitude(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field longitude"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_double

    def _mod_longitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_double

    def _del_longitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "longitude"

    longitude = property(_get_longitude, _set_longitude, _del_longitude)

    @property
    def longitude__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def longitude__type(self):
        return ProtoBase.TYPE_double

    def _finalize_longitude(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_longitude)


TYPE_SpawnPoint = SpawnPoint
_PB_finalizers.append('SpawnPoint')

class FortSummary(ProtoBase):
    _required = []
    _field_map = {'last_modified_timestamp_ms': 2, 'latitude': 3, 'fort_summary_id': 1, 'longitude': 4}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['fort_summary_id', 'last_modified_timestamp_ms', 'latitude', 'longitude']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_fort_summary_id(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_int32, 'fort_summary_id')
            self._cache[1] = r
        return r

    def _establish_parentage_fort_summary_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_fort_summary_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_fort_summary_id
                v._pbf_establish_parent_callback = self._establish_parentage_fort_summary_id

    def _set_fort_summary_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_fort_summary_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field fort_summary_id"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_int32

    def _mod_fort_summary_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_int32

    def _del_fort_summary_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "fort_summary_id"

    fort_summary_id = property(_get_fort_summary_id, _set_fort_summary_id, _del_fort_summary_id)

    @property
    def fort_summary_id__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def fort_summary_id__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_fort_summary_id(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_fort_summary_id)


    def _get_last_modified_timestamp_ms(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int32, 'last_modified_timestamp_ms')
            self._cache[2] = r
        return r

    def _establish_parentage_last_modified_timestamp_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_last_modified_timestamp_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_last_modified_timestamp_ms
                v._pbf_establish_parent_callback = self._establish_parentage_last_modified_timestamp_ms

    def _set_last_modified_timestamp_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_last_modified_timestamp_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field last_modified_timestamp_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_int32

    def _mod_last_modified_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int32

    def _del_last_modified_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "last_modified_timestamp_ms"

    last_modified_timestamp_ms = property(_get_last_modified_timestamp_ms, _set_last_modified_timestamp_ms, _del_last_modified_timestamp_ms)

    @property
    def last_modified_timestamp_ms__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def last_modified_timestamp_ms__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_last_modified_timestamp_ms(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_last_modified_timestamp_ms)


    def _get_latitude(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_int32, 'latitude')
            self._cache[3] = r
        return r

    def _establish_parentage_latitude(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_latitude), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_latitude
                v._pbf_establish_parent_callback = self._establish_parentage_latitude

    def _set_latitude(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_latitude(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field latitude"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_int32

    def _mod_latitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_int32

    def _del_latitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "latitude"

    latitude = property(_get_latitude, _set_latitude, _del_latitude)

    @property
    def latitude__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def latitude__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_latitude(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_latitude)


    def _get_longitude(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, ProtoBase.TYPE_int32, 'longitude')
            self._cache[4] = r
        return r

    def _establish_parentage_longitude(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_longitude), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_longitude
                v._pbf_establish_parent_callback = self._establish_parentage_longitude

    def _set_longitude(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_longitude(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field longitude"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = ProtoBase.TYPE_int32

    def _mod_longitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = ProtoBase.TYPE_int32

    def _del_longitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "longitude"

    longitude = property(_get_longitude, _set_longitude, _del_longitude)

    @property
    def longitude__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def longitude__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_longitude(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(4)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_longitude)


TYPE_FortSummary = FortSummary
_PB_finalizers.append('FortSummary')

class WildPokemon(ProtoBase):
    _required = []
    _field_map = {'last_modified_timestamp_ms': 2, 'spawnpoint_id': 5, 'longitude': 4, 'pokemon_data': 7, 'latitude': 3, 'encounter_id': 1, 'time_till_hidden_ms': 11}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['encounter_id', 'last_modified_timestamp_ms', 'latitude', 'longitude', 'spawnpoint_id', 'pokemon_data', 'time_till_hidden_ms']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_encounter_id(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_fixed64, 'encounter_id')
            self._cache[1] = r
        return r

    def _establish_parentage_encounter_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_encounter_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_encounter_id
                v._pbf_establish_parent_callback = self._establish_parentage_encounter_id

    def _set_encounter_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_encounter_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field encounter_id"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_fixed64

    def _mod_encounter_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_fixed64

    def _del_encounter_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "encounter_id"

    encounter_id = property(_get_encounter_id, _set_encounter_id, _del_encounter_id)

    @property
    def encounter_id__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def encounter_id__type(self):
        return ProtoBase.TYPE_fixed64

    def _finalize_encounter_id(cls):
        if is_string(ProtoBase.TYPE_fixed64):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_fixed64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_fixed64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_fixed64.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_encounter_id)


    def _get_last_modified_timestamp_ms(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int64, 'last_modified_timestamp_ms')
            self._cache[2] = r
        return r

    def _establish_parentage_last_modified_timestamp_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_last_modified_timestamp_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_last_modified_timestamp_ms
                v._pbf_establish_parent_callback = self._establish_parentage_last_modified_timestamp_ms

    def _set_last_modified_timestamp_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_last_modified_timestamp_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field last_modified_timestamp_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_int64

    def _mod_last_modified_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int64

    def _del_last_modified_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "last_modified_timestamp_ms"

    last_modified_timestamp_ms = property(_get_last_modified_timestamp_ms, _set_last_modified_timestamp_ms, _del_last_modified_timestamp_ms)

    @property
    def last_modified_timestamp_ms__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def last_modified_timestamp_ms__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_last_modified_timestamp_ms(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_last_modified_timestamp_ms)


    def _get_latitude(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_double, 'latitude')
            self._cache[3] = r
        return r

    def _establish_parentage_latitude(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_latitude), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_latitude
                v._pbf_establish_parent_callback = self._establish_parentage_latitude

    def _set_latitude(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_latitude(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field latitude"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_double

    def _mod_latitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_double

    def _del_latitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "latitude"

    latitude = property(_get_latitude, _set_latitude, _del_latitude)

    @property
    def latitude__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def latitude__type(self):
        return ProtoBase.TYPE_double

    def _finalize_latitude(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_latitude)


    def _get_longitude(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, ProtoBase.TYPE_double, 'longitude')
            self._cache[4] = r
        return r

    def _establish_parentage_longitude(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_longitude), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_longitude
                v._pbf_establish_parent_callback = self._establish_parentage_longitude

    def _set_longitude(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_longitude(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field longitude"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = ProtoBase.TYPE_double

    def _mod_longitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = ProtoBase.TYPE_double

    def _del_longitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "longitude"

    longitude = property(_get_longitude, _set_longitude, _del_longitude)

    @property
    def longitude__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def longitude__type(self):
        return ProtoBase.TYPE_double

    def _finalize_longitude(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(4)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_longitude)


    def _get_spawnpoint_id(self):
        if 5 in self._cache:
            r = self._cache[5]
        else:
            r = self._buf_get(5, ProtoBase.TYPE_string, 'spawnpoint_id')
            self._cache[5] = r
        return r

    def _establish_parentage_spawnpoint_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_spawnpoint_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_spawnpoint_id
                v._pbf_establish_parent_callback = self._establish_parentage_spawnpoint_id

    def _set_spawnpoint_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_spawnpoint_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field spawnpoint_id"
            raise ProtoValueError(list_assign_error)
        self._cache[5] = v
        self._mods[5] = ProtoBase.TYPE_string

    def _mod_spawnpoint_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[5] = ProtoBase.TYPE_string

    def _del_spawnpoint_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 5 in self._cache:
            del self._cache[5]
        if 5 in self._mods:
            del self._mods[5]
        self._buf_del(5)

    _pb_field_name_5 = "spawnpoint_id"

    spawnpoint_id = property(_get_spawnpoint_id, _set_spawnpoint_id, _del_spawnpoint_id)

    @property
    def spawnpoint_id__exists(self):
        return 5 in self._mods or self._buf_exists(5)

    @property
    def spawnpoint_id__type(self):
        return ProtoBase.TYPE_string

    def _finalize_spawnpoint_id(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(5)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(5)

    _pbf_finalizers.append(_finalize_spawnpoint_id)


    def _get_pokemon_data(self):
        if 7 in self._cache:
            r = self._cache[7]
        else:
            r = self._buf_get(7, TYPE_PokemonData, 'pokemon_data')
            self._cache[7] = r
        return r

    def _establish_parentage_pokemon_data(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokemon_data), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokemon_data
                v._pbf_establish_parent_callback = self._establish_parentage_pokemon_data

    def _set_pokemon_data(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokemon_data(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokemon_data"
            raise ProtoValueError(list_assign_error)
        self._cache[7] = v
        self._mods[7] = TYPE_PokemonData

    def _mod_pokemon_data(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[7] = TYPE_PokemonData

    def _del_pokemon_data(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 7 in self._cache:
            del self._cache[7]
        if 7 in self._mods:
            del self._mods[7]
        self._buf_del(7)

    _pb_field_name_7 = "pokemon_data"

    pokemon_data = property(_get_pokemon_data, _set_pokemon_data, _del_pokemon_data)

    @property
    def pokemon_data__exists(self):
        return 7 in self._mods or self._buf_exists(7)

    @property
    def pokemon_data__type(self):
        return TYPE_PokemonData

    def _finalize_pokemon_data(cls):
        if is_string(TYPE_PokemonData):
            cls._pbf_strings.append(7)
        elif _PB_type(TYPE_PokemonData) is _PB_type:
            assert issubclass(TYPE_PokemonData, RepeatedSequence)
            if is_string(TYPE_PokemonData.pb_subtype):
                cls._pbf_strings.append(7)

    _pbf_finalizers.append(_finalize_pokemon_data)


    def _get_time_till_hidden_ms(self):
        if 11 in self._cache:
            r = self._cache[11]
        else:
            r = self._buf_get(11, ProtoBase.TYPE_int32, 'time_till_hidden_ms')
            self._cache[11] = r
        return r

    def _establish_parentage_time_till_hidden_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_time_till_hidden_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_time_till_hidden_ms
                v._pbf_establish_parent_callback = self._establish_parentage_time_till_hidden_ms

    def _set_time_till_hidden_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_time_till_hidden_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field time_till_hidden_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[11] = v
        self._mods[11] = ProtoBase.TYPE_int32

    def _mod_time_till_hidden_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[11] = ProtoBase.TYPE_int32

    def _del_time_till_hidden_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 11 in self._cache:
            del self._cache[11]
        if 11 in self._mods:
            del self._mods[11]
        self._buf_del(11)

    _pb_field_name_11 = "time_till_hidden_ms"

    time_till_hidden_ms = property(_get_time_till_hidden_ms, _set_time_till_hidden_ms, _del_time_till_hidden_ms)

    @property
    def time_till_hidden_ms__exists(self):
        return 11 in self._mods or self._buf_exists(11)

    @property
    def time_till_hidden_ms__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_time_till_hidden_ms(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(11)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(11)

    _pbf_finalizers.append(_finalize_time_till_hidden_ms)


TYPE_WildPokemon = WildPokemon
_PB_finalizers.append('WildPokemon')

class PokemonData(ProtoBase):
    _required = []
    _field_map = {'origin': 14, 'is_egg': 10, 'egg_km_walked_target': 11, 'creation_time_ms': 26, 'cp_multiplier': 20, 'cp': 3, 'id': 1, 'move_1': 6, 'move_2': 7, 'pokemon_id': 2, 'individual_stamina': 19, 'stamina': 4, 'individual_attack': 17, 'owner_name': 9, 'stamina_max': 5, 'weight_kg': 16, 'battles_attacked': 23, 'nickname': 30, 'from_fort': 31, 'num_upgrades': 27, 'individual_defense': 18, 'additional_cp_multiplier': 28, 'pokeball': 21, 'egg_incubator_id': 25, 'height_m': 15, 'captured_cell_id': 22, 'favorite': 29, 'egg_km_walked_start': 12, 'battles_defended': 24, 'deployed_fort_id': 8}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['id', 'pokemon_id', 'cp', 'stamina', 'stamina_max', 'move_1', 'move_2', 'deployed_fort_id', 'owner_name', 'is_egg', 'egg_km_walked_target', 'egg_km_walked_start', 'origin', 'height_m', 'weight_kg', 'individual_attack', 'individual_defense', 'individual_stamina', 'cp_multiplier', 'pokeball', 'captured_cell_id', 'battles_attacked', 'battles_defended', 'egg_incubator_id', 'creation_time_ms', 'num_upgrades', 'additional_cp_multiplier', 'favorite', 'nickname', 'from_fort']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_id(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_int32, 'id')
            self._cache[1] = r
        return r

    def _establish_parentage_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_id
                v._pbf_establish_parent_callback = self._establish_parentage_id

    def _set_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field id"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_int32

    def _mod_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_int32

    def _del_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "id"

    id = property(_get_id, _set_id, _del_id)

    @property
    def id__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def id__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_id(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_id)


    def _get_pokemon_id(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, RpcEnum_palm.TYPE_PokemonId, 'pokemon_id')
            self._cache[2] = r
        return r

    def _establish_parentage_pokemon_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokemon_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokemon_id
                v._pbf_establish_parent_callback = self._establish_parentage_pokemon_id

    def _set_pokemon_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokemon_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokemon_id"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = RpcEnum_palm.TYPE_PokemonId

    def _mod_pokemon_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = RpcEnum_palm.TYPE_PokemonId

    def _del_pokemon_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "pokemon_id"

    pokemon_id = property(_get_pokemon_id, _set_pokemon_id, _del_pokemon_id)

    @property
    def pokemon_id__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def pokemon_id__type(self):
        return RpcEnum_palm.TYPE_PokemonId

    def _finalize_pokemon_id(cls):
        if is_string(RpcEnum_palm.TYPE_PokemonId):
            cls._pbf_strings.append(2)
        elif _PB_type(RpcEnum_palm.TYPE_PokemonId) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_PokemonId, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_PokemonId.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_pokemon_id)


    def _get_cp(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_int32, 'cp')
            self._cache[3] = r
        return r

    def _establish_parentage_cp(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_cp), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_cp
                v._pbf_establish_parent_callback = self._establish_parentage_cp

    def _set_cp(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_cp(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field cp"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_int32

    def _mod_cp(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_int32

    def _del_cp(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "cp"

    cp = property(_get_cp, _set_cp, _del_cp)

    @property
    def cp__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def cp__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_cp(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_cp)


    def _get_stamina(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, ProtoBase.TYPE_int32, 'stamina')
            self._cache[4] = r
        return r

    def _establish_parentage_stamina(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_stamina), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_stamina
                v._pbf_establish_parent_callback = self._establish_parentage_stamina

    def _set_stamina(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_stamina(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field stamina"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = ProtoBase.TYPE_int32

    def _mod_stamina(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = ProtoBase.TYPE_int32

    def _del_stamina(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "stamina"

    stamina = property(_get_stamina, _set_stamina, _del_stamina)

    @property
    def stamina__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def stamina__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_stamina(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(4)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_stamina)


    def _get_stamina_max(self):
        if 5 in self._cache:
            r = self._cache[5]
        else:
            r = self._buf_get(5, ProtoBase.TYPE_int32, 'stamina_max')
            self._cache[5] = r
        return r

    def _establish_parentage_stamina_max(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_stamina_max), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_stamina_max
                v._pbf_establish_parent_callback = self._establish_parentage_stamina_max

    def _set_stamina_max(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_stamina_max(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field stamina_max"
            raise ProtoValueError(list_assign_error)
        self._cache[5] = v
        self._mods[5] = ProtoBase.TYPE_int32

    def _mod_stamina_max(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[5] = ProtoBase.TYPE_int32

    def _del_stamina_max(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 5 in self._cache:
            del self._cache[5]
        if 5 in self._mods:
            del self._mods[5]
        self._buf_del(5)

    _pb_field_name_5 = "stamina_max"

    stamina_max = property(_get_stamina_max, _set_stamina_max, _del_stamina_max)

    @property
    def stamina_max__exists(self):
        return 5 in self._mods or self._buf_exists(5)

    @property
    def stamina_max__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_stamina_max(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(5)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(5)

    _pbf_finalizers.append(_finalize_stamina_max)


    def _get_move_1(self):
        if 6 in self._cache:
            r = self._cache[6]
        else:
            r = self._buf_get(6, RpcEnum_palm.TYPE_PokemonMove, 'move_1')
            self._cache[6] = r
        return r

    def _establish_parentage_move_1(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_move_1), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_move_1
                v._pbf_establish_parent_callback = self._establish_parentage_move_1

    def _set_move_1(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_move_1(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field move_1"
            raise ProtoValueError(list_assign_error)
        self._cache[6] = v
        self._mods[6] = RpcEnum_palm.TYPE_PokemonMove

    def _mod_move_1(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[6] = RpcEnum_palm.TYPE_PokemonMove

    def _del_move_1(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 6 in self._cache:
            del self._cache[6]
        if 6 in self._mods:
            del self._mods[6]
        self._buf_del(6)

    _pb_field_name_6 = "move_1"

    move_1 = property(_get_move_1, _set_move_1, _del_move_1)

    @property
    def move_1__exists(self):
        return 6 in self._mods or self._buf_exists(6)

    @property
    def move_1__type(self):
        return RpcEnum_palm.TYPE_PokemonMove

    def _finalize_move_1(cls):
        if is_string(RpcEnum_palm.TYPE_PokemonMove):
            cls._pbf_strings.append(6)
        elif _PB_type(RpcEnum_palm.TYPE_PokemonMove) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_PokemonMove, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_PokemonMove.pb_subtype):
                cls._pbf_strings.append(6)

    _pbf_finalizers.append(_finalize_move_1)


    def _get_move_2(self):
        if 7 in self._cache:
            r = self._cache[7]
        else:
            r = self._buf_get(7, RpcEnum_palm.TYPE_PokemonMove, 'move_2')
            self._cache[7] = r
        return r

    def _establish_parentage_move_2(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_move_2), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_move_2
                v._pbf_establish_parent_callback = self._establish_parentage_move_2

    def _set_move_2(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_move_2(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field move_2"
            raise ProtoValueError(list_assign_error)
        self._cache[7] = v
        self._mods[7] = RpcEnum_palm.TYPE_PokemonMove

    def _mod_move_2(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[7] = RpcEnum_palm.TYPE_PokemonMove

    def _del_move_2(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 7 in self._cache:
            del self._cache[7]
        if 7 in self._mods:
            del self._mods[7]
        self._buf_del(7)

    _pb_field_name_7 = "move_2"

    move_2 = property(_get_move_2, _set_move_2, _del_move_2)

    @property
    def move_2__exists(self):
        return 7 in self._mods or self._buf_exists(7)

    @property
    def move_2__type(self):
        return RpcEnum_palm.TYPE_PokemonMove

    def _finalize_move_2(cls):
        if is_string(RpcEnum_palm.TYPE_PokemonMove):
            cls._pbf_strings.append(7)
        elif _PB_type(RpcEnum_palm.TYPE_PokemonMove) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_PokemonMove, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_PokemonMove.pb_subtype):
                cls._pbf_strings.append(7)

    _pbf_finalizers.append(_finalize_move_2)


    def _get_deployed_fort_id(self):
        if 8 in self._cache:
            r = self._cache[8]
        else:
            r = self._buf_get(8, ProtoBase.TYPE_int32, 'deployed_fort_id')
            self._cache[8] = r
        return r

    def _establish_parentage_deployed_fort_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_deployed_fort_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_deployed_fort_id
                v._pbf_establish_parent_callback = self._establish_parentage_deployed_fort_id

    def _set_deployed_fort_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_deployed_fort_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field deployed_fort_id"
            raise ProtoValueError(list_assign_error)
        self._cache[8] = v
        self._mods[8] = ProtoBase.TYPE_int32

    def _mod_deployed_fort_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[8] = ProtoBase.TYPE_int32

    def _del_deployed_fort_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 8 in self._cache:
            del self._cache[8]
        if 8 in self._mods:
            del self._mods[8]
        self._buf_del(8)

    _pb_field_name_8 = "deployed_fort_id"

    deployed_fort_id = property(_get_deployed_fort_id, _set_deployed_fort_id, _del_deployed_fort_id)

    @property
    def deployed_fort_id__exists(self):
        return 8 in self._mods or self._buf_exists(8)

    @property
    def deployed_fort_id__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_deployed_fort_id(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(8)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(8)

    _pbf_finalizers.append(_finalize_deployed_fort_id)


    def _get_owner_name(self):
        if 9 in self._cache:
            r = self._cache[9]
        else:
            r = self._buf_get(9, ProtoBase.TYPE_string, 'owner_name')
            self._cache[9] = r
        return r

    def _establish_parentage_owner_name(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_owner_name), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_owner_name
                v._pbf_establish_parent_callback = self._establish_parentage_owner_name

    def _set_owner_name(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_owner_name(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field owner_name"
            raise ProtoValueError(list_assign_error)
        self._cache[9] = v
        self._mods[9] = ProtoBase.TYPE_string

    def _mod_owner_name(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[9] = ProtoBase.TYPE_string

    def _del_owner_name(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 9 in self._cache:
            del self._cache[9]
        if 9 in self._mods:
            del self._mods[9]
        self._buf_del(9)

    _pb_field_name_9 = "owner_name"

    owner_name = property(_get_owner_name, _set_owner_name, _del_owner_name)

    @property
    def owner_name__exists(self):
        return 9 in self._mods or self._buf_exists(9)

    @property
    def owner_name__type(self):
        return ProtoBase.TYPE_string

    def _finalize_owner_name(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(9)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(9)

    _pbf_finalizers.append(_finalize_owner_name)


    def _get_is_egg(self):
        if 10 in self._cache:
            r = self._cache[10]
        else:
            r = self._buf_get(10, ProtoBase.TYPE_bool, 'is_egg')
            self._cache[10] = r
        return r

    def _establish_parentage_is_egg(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_is_egg), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_is_egg
                v._pbf_establish_parent_callback = self._establish_parentage_is_egg

    def _set_is_egg(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_is_egg(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field is_egg"
            raise ProtoValueError(list_assign_error)
        self._cache[10] = v
        self._mods[10] = ProtoBase.TYPE_bool

    def _mod_is_egg(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[10] = ProtoBase.TYPE_bool

    def _del_is_egg(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 10 in self._cache:
            del self._cache[10]
        if 10 in self._mods:
            del self._mods[10]
        self._buf_del(10)

    _pb_field_name_10 = "is_egg"

    is_egg = property(_get_is_egg, _set_is_egg, _del_is_egg)

    @property
    def is_egg__exists(self):
        return 10 in self._mods or self._buf_exists(10)

    @property
    def is_egg__type(self):
        return ProtoBase.TYPE_bool

    def _finalize_is_egg(cls):
        if is_string(ProtoBase.TYPE_bool):
            cls._pbf_strings.append(10)
        elif _PB_type(ProtoBase.TYPE_bool) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bool, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bool.pb_subtype):
                cls._pbf_strings.append(10)

    _pbf_finalizers.append(_finalize_is_egg)


    def _get_egg_km_walked_target(self):
        if 11 in self._cache:
            r = self._cache[11]
        else:
            r = self._buf_get(11, ProtoBase.TYPE_int32, 'egg_km_walked_target')
            self._cache[11] = r
        return r

    def _establish_parentage_egg_km_walked_target(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_egg_km_walked_target), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_egg_km_walked_target
                v._pbf_establish_parent_callback = self._establish_parentage_egg_km_walked_target

    def _set_egg_km_walked_target(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_egg_km_walked_target(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field egg_km_walked_target"
            raise ProtoValueError(list_assign_error)
        self._cache[11] = v
        self._mods[11] = ProtoBase.TYPE_int32

    def _mod_egg_km_walked_target(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[11] = ProtoBase.TYPE_int32

    def _del_egg_km_walked_target(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 11 in self._cache:
            del self._cache[11]
        if 11 in self._mods:
            del self._mods[11]
        self._buf_del(11)

    _pb_field_name_11 = "egg_km_walked_target"

    egg_km_walked_target = property(_get_egg_km_walked_target, _set_egg_km_walked_target, _del_egg_km_walked_target)

    @property
    def egg_km_walked_target__exists(self):
        return 11 in self._mods or self._buf_exists(11)

    @property
    def egg_km_walked_target__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_egg_km_walked_target(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(11)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(11)

    _pbf_finalizers.append(_finalize_egg_km_walked_target)


    def _get_egg_km_walked_start(self):
        if 12 in self._cache:
            r = self._cache[12]
        else:
            r = self._buf_get(12, ProtoBase.TYPE_int32, 'egg_km_walked_start')
            self._cache[12] = r
        return r

    def _establish_parentage_egg_km_walked_start(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_egg_km_walked_start), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_egg_km_walked_start
                v._pbf_establish_parent_callback = self._establish_parentage_egg_km_walked_start

    def _set_egg_km_walked_start(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_egg_km_walked_start(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field egg_km_walked_start"
            raise ProtoValueError(list_assign_error)
        self._cache[12] = v
        self._mods[12] = ProtoBase.TYPE_int32

    def _mod_egg_km_walked_start(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[12] = ProtoBase.TYPE_int32

    def _del_egg_km_walked_start(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 12 in self._cache:
            del self._cache[12]
        if 12 in self._mods:
            del self._mods[12]
        self._buf_del(12)

    _pb_field_name_12 = "egg_km_walked_start"

    egg_km_walked_start = property(_get_egg_km_walked_start, _set_egg_km_walked_start, _del_egg_km_walked_start)

    @property
    def egg_km_walked_start__exists(self):
        return 12 in self._mods or self._buf_exists(12)

    @property
    def egg_km_walked_start__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_egg_km_walked_start(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(12)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(12)

    _pbf_finalizers.append(_finalize_egg_km_walked_start)


    def _get_origin(self):
        if 14 in self._cache:
            r = self._cache[14]
        else:
            r = self._buf_get(14, ProtoBase.TYPE_int32, 'origin')
            self._cache[14] = r
        return r

    def _establish_parentage_origin(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_origin), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_origin
                v._pbf_establish_parent_callback = self._establish_parentage_origin

    def _set_origin(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_origin(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field origin"
            raise ProtoValueError(list_assign_error)
        self._cache[14] = v
        self._mods[14] = ProtoBase.TYPE_int32

    def _mod_origin(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[14] = ProtoBase.TYPE_int32

    def _del_origin(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 14 in self._cache:
            del self._cache[14]
        if 14 in self._mods:
            del self._mods[14]
        self._buf_del(14)

    _pb_field_name_14 = "origin"

    origin = property(_get_origin, _set_origin, _del_origin)

    @property
    def origin__exists(self):
        return 14 in self._mods or self._buf_exists(14)

    @property
    def origin__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_origin(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(14)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(14)

    _pbf_finalizers.append(_finalize_origin)


    def _get_height_m(self):
        if 15 in self._cache:
            r = self._cache[15]
        else:
            r = self._buf_get(15, ProtoBase.TYPE_float, 'height_m')
            self._cache[15] = r
        return r

    def _establish_parentage_height_m(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_height_m), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_height_m
                v._pbf_establish_parent_callback = self._establish_parentage_height_m

    def _set_height_m(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_height_m(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field height_m"
            raise ProtoValueError(list_assign_error)
        self._cache[15] = v
        self._mods[15] = ProtoBase.TYPE_float

    def _mod_height_m(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[15] = ProtoBase.TYPE_float

    def _del_height_m(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 15 in self._cache:
            del self._cache[15]
        if 15 in self._mods:
            del self._mods[15]
        self._buf_del(15)

    _pb_field_name_15 = "height_m"

    height_m = property(_get_height_m, _set_height_m, _del_height_m)

    @property
    def height_m__exists(self):
        return 15 in self._mods or self._buf_exists(15)

    @property
    def height_m__type(self):
        return ProtoBase.TYPE_float

    def _finalize_height_m(cls):
        if is_string(ProtoBase.TYPE_float):
            cls._pbf_strings.append(15)
        elif _PB_type(ProtoBase.TYPE_float) is _PB_type:
            assert issubclass(ProtoBase.TYPE_float, RepeatedSequence)
            if is_string(ProtoBase.TYPE_float.pb_subtype):
                cls._pbf_strings.append(15)

    _pbf_finalizers.append(_finalize_height_m)


    def _get_weight_kg(self):
        if 16 in self._cache:
            r = self._cache[16]
        else:
            r = self._buf_get(16, ProtoBase.TYPE_float, 'weight_kg')
            self._cache[16] = r
        return r

    def _establish_parentage_weight_kg(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_weight_kg), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_weight_kg
                v._pbf_establish_parent_callback = self._establish_parentage_weight_kg

    def _set_weight_kg(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_weight_kg(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field weight_kg"
            raise ProtoValueError(list_assign_error)
        self._cache[16] = v
        self._mods[16] = ProtoBase.TYPE_float

    def _mod_weight_kg(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[16] = ProtoBase.TYPE_float

    def _del_weight_kg(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 16 in self._cache:
            del self._cache[16]
        if 16 in self._mods:
            del self._mods[16]
        self._buf_del(16)

    _pb_field_name_16 = "weight_kg"

    weight_kg = property(_get_weight_kg, _set_weight_kg, _del_weight_kg)

    @property
    def weight_kg__exists(self):
        return 16 in self._mods or self._buf_exists(16)

    @property
    def weight_kg__type(self):
        return ProtoBase.TYPE_float

    def _finalize_weight_kg(cls):
        if is_string(ProtoBase.TYPE_float):
            cls._pbf_strings.append(16)
        elif _PB_type(ProtoBase.TYPE_float) is _PB_type:
            assert issubclass(ProtoBase.TYPE_float, RepeatedSequence)
            if is_string(ProtoBase.TYPE_float.pb_subtype):
                cls._pbf_strings.append(16)

    _pbf_finalizers.append(_finalize_weight_kg)


    def _get_individual_attack(self):
        if 17 in self._cache:
            r = self._cache[17]
        else:
            r = self._buf_get(17, ProtoBase.TYPE_int32, 'individual_attack')
            self._cache[17] = r
        return r

    def _establish_parentage_individual_attack(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_individual_attack), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_individual_attack
                v._pbf_establish_parent_callback = self._establish_parentage_individual_attack

    def _set_individual_attack(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_individual_attack(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field individual_attack"
            raise ProtoValueError(list_assign_error)
        self._cache[17] = v
        self._mods[17] = ProtoBase.TYPE_int32

    def _mod_individual_attack(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[17] = ProtoBase.TYPE_int32

    def _del_individual_attack(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 17 in self._cache:
            del self._cache[17]
        if 17 in self._mods:
            del self._mods[17]
        self._buf_del(17)

    _pb_field_name_17 = "individual_attack"

    individual_attack = property(_get_individual_attack, _set_individual_attack, _del_individual_attack)

    @property
    def individual_attack__exists(self):
        return 17 in self._mods or self._buf_exists(17)

    @property
    def individual_attack__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_individual_attack(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(17)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(17)

    _pbf_finalizers.append(_finalize_individual_attack)


    def _get_individual_defense(self):
        if 18 in self._cache:
            r = self._cache[18]
        else:
            r = self._buf_get(18, ProtoBase.TYPE_int32, 'individual_defense')
            self._cache[18] = r
        return r

    def _establish_parentage_individual_defense(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_individual_defense), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_individual_defense
                v._pbf_establish_parent_callback = self._establish_parentage_individual_defense

    def _set_individual_defense(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_individual_defense(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field individual_defense"
            raise ProtoValueError(list_assign_error)
        self._cache[18] = v
        self._mods[18] = ProtoBase.TYPE_int32

    def _mod_individual_defense(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[18] = ProtoBase.TYPE_int32

    def _del_individual_defense(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 18 in self._cache:
            del self._cache[18]
        if 18 in self._mods:
            del self._mods[18]
        self._buf_del(18)

    _pb_field_name_18 = "individual_defense"

    individual_defense = property(_get_individual_defense, _set_individual_defense, _del_individual_defense)

    @property
    def individual_defense__exists(self):
        return 18 in self._mods or self._buf_exists(18)

    @property
    def individual_defense__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_individual_defense(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(18)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(18)

    _pbf_finalizers.append(_finalize_individual_defense)


    def _get_individual_stamina(self):
        if 19 in self._cache:
            r = self._cache[19]
        else:
            r = self._buf_get(19, ProtoBase.TYPE_int32, 'individual_stamina')
            self._cache[19] = r
        return r

    def _establish_parentage_individual_stamina(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_individual_stamina), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_individual_stamina
                v._pbf_establish_parent_callback = self._establish_parentage_individual_stamina

    def _set_individual_stamina(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_individual_stamina(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field individual_stamina"
            raise ProtoValueError(list_assign_error)
        self._cache[19] = v
        self._mods[19] = ProtoBase.TYPE_int32

    def _mod_individual_stamina(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[19] = ProtoBase.TYPE_int32

    def _del_individual_stamina(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 19 in self._cache:
            del self._cache[19]
        if 19 in self._mods:
            del self._mods[19]
        self._buf_del(19)

    _pb_field_name_19 = "individual_stamina"

    individual_stamina = property(_get_individual_stamina, _set_individual_stamina, _del_individual_stamina)

    @property
    def individual_stamina__exists(self):
        return 19 in self._mods or self._buf_exists(19)

    @property
    def individual_stamina__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_individual_stamina(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(19)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(19)

    _pbf_finalizers.append(_finalize_individual_stamina)


    def _get_cp_multiplier(self):
        if 20 in self._cache:
            r = self._cache[20]
        else:
            r = self._buf_get(20, ProtoBase.TYPE_int32, 'cp_multiplier')
            self._cache[20] = r
        return r

    def _establish_parentage_cp_multiplier(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_cp_multiplier), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_cp_multiplier
                v._pbf_establish_parent_callback = self._establish_parentage_cp_multiplier

    def _set_cp_multiplier(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_cp_multiplier(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field cp_multiplier"
            raise ProtoValueError(list_assign_error)
        self._cache[20] = v
        self._mods[20] = ProtoBase.TYPE_int32

    def _mod_cp_multiplier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[20] = ProtoBase.TYPE_int32

    def _del_cp_multiplier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 20 in self._cache:
            del self._cache[20]
        if 20 in self._mods:
            del self._mods[20]
        self._buf_del(20)

    _pb_field_name_20 = "cp_multiplier"

    cp_multiplier = property(_get_cp_multiplier, _set_cp_multiplier, _del_cp_multiplier)

    @property
    def cp_multiplier__exists(self):
        return 20 in self._mods or self._buf_exists(20)

    @property
    def cp_multiplier__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_cp_multiplier(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(20)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(20)

    _pbf_finalizers.append(_finalize_cp_multiplier)


    def _get_pokeball(self):
        if 21 in self._cache:
            r = self._cache[21]
        else:
            r = self._buf_get(21, ProtoBase.TYPE_int32, 'pokeball')
            self._cache[21] = r
        return r

    def _establish_parentage_pokeball(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokeball), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokeball
                v._pbf_establish_parent_callback = self._establish_parentage_pokeball

    def _set_pokeball(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokeball(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokeball"
            raise ProtoValueError(list_assign_error)
        self._cache[21] = v
        self._mods[21] = ProtoBase.TYPE_int32

    def _mod_pokeball(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[21] = ProtoBase.TYPE_int32

    def _del_pokeball(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 21 in self._cache:
            del self._cache[21]
        if 21 in self._mods:
            del self._mods[21]
        self._buf_del(21)

    _pb_field_name_21 = "pokeball"

    pokeball = property(_get_pokeball, _set_pokeball, _del_pokeball)

    @property
    def pokeball__exists(self):
        return 21 in self._mods or self._buf_exists(21)

    @property
    def pokeball__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_pokeball(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(21)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(21)

    _pbf_finalizers.append(_finalize_pokeball)


    def _get_captured_cell_id(self):
        if 22 in self._cache:
            r = self._cache[22]
        else:
            r = self._buf_get(22, ProtoBase.TYPE_uint64, 'captured_cell_id')
            self._cache[22] = r
        return r

    def _establish_parentage_captured_cell_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_captured_cell_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_captured_cell_id
                v._pbf_establish_parent_callback = self._establish_parentage_captured_cell_id

    def _set_captured_cell_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_captured_cell_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field captured_cell_id"
            raise ProtoValueError(list_assign_error)
        self._cache[22] = v
        self._mods[22] = ProtoBase.TYPE_uint64

    def _mod_captured_cell_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[22] = ProtoBase.TYPE_uint64

    def _del_captured_cell_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 22 in self._cache:
            del self._cache[22]
        if 22 in self._mods:
            del self._mods[22]
        self._buf_del(22)

    _pb_field_name_22 = "captured_cell_id"

    captured_cell_id = property(_get_captured_cell_id, _set_captured_cell_id, _del_captured_cell_id)

    @property
    def captured_cell_id__exists(self):
        return 22 in self._mods or self._buf_exists(22)

    @property
    def captured_cell_id__type(self):
        return ProtoBase.TYPE_uint64

    def _finalize_captured_cell_id(cls):
        if is_string(ProtoBase.TYPE_uint64):
            cls._pbf_strings.append(22)
        elif _PB_type(ProtoBase.TYPE_uint64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_uint64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_uint64.pb_subtype):
                cls._pbf_strings.append(22)

    _pbf_finalizers.append(_finalize_captured_cell_id)


    def _get_battles_attacked(self):
        if 23 in self._cache:
            r = self._cache[23]
        else:
            r = self._buf_get(23, ProtoBase.TYPE_int32, 'battles_attacked')
            self._cache[23] = r
        return r

    def _establish_parentage_battles_attacked(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_battles_attacked), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_battles_attacked
                v._pbf_establish_parent_callback = self._establish_parentage_battles_attacked

    def _set_battles_attacked(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_battles_attacked(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field battles_attacked"
            raise ProtoValueError(list_assign_error)
        self._cache[23] = v
        self._mods[23] = ProtoBase.TYPE_int32

    def _mod_battles_attacked(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[23] = ProtoBase.TYPE_int32

    def _del_battles_attacked(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 23 in self._cache:
            del self._cache[23]
        if 23 in self._mods:
            del self._mods[23]
        self._buf_del(23)

    _pb_field_name_23 = "battles_attacked"

    battles_attacked = property(_get_battles_attacked, _set_battles_attacked, _del_battles_attacked)

    @property
    def battles_attacked__exists(self):
        return 23 in self._mods or self._buf_exists(23)

    @property
    def battles_attacked__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_battles_attacked(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(23)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(23)

    _pbf_finalizers.append(_finalize_battles_attacked)


    def _get_battles_defended(self):
        if 24 in self._cache:
            r = self._cache[24]
        else:
            r = self._buf_get(24, ProtoBase.TYPE_int32, 'battles_defended')
            self._cache[24] = r
        return r

    def _establish_parentage_battles_defended(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_battles_defended), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_battles_defended
                v._pbf_establish_parent_callback = self._establish_parentage_battles_defended

    def _set_battles_defended(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_battles_defended(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field battles_defended"
            raise ProtoValueError(list_assign_error)
        self._cache[24] = v
        self._mods[24] = ProtoBase.TYPE_int32

    def _mod_battles_defended(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[24] = ProtoBase.TYPE_int32

    def _del_battles_defended(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 24 in self._cache:
            del self._cache[24]
        if 24 in self._mods:
            del self._mods[24]
        self._buf_del(24)

    _pb_field_name_24 = "battles_defended"

    battles_defended = property(_get_battles_defended, _set_battles_defended, _del_battles_defended)

    @property
    def battles_defended__exists(self):
        return 24 in self._mods or self._buf_exists(24)

    @property
    def battles_defended__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_battles_defended(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(24)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(24)

    _pbf_finalizers.append(_finalize_battles_defended)


    def _get_egg_incubator_id(self):
        if 25 in self._cache:
            r = self._cache[25]
        else:
            r = self._buf_get(25, ProtoBase.TYPE_int32, 'egg_incubator_id')
            self._cache[25] = r
        return r

    def _establish_parentage_egg_incubator_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_egg_incubator_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_egg_incubator_id
                v._pbf_establish_parent_callback = self._establish_parentage_egg_incubator_id

    def _set_egg_incubator_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_egg_incubator_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field egg_incubator_id"
            raise ProtoValueError(list_assign_error)
        self._cache[25] = v
        self._mods[25] = ProtoBase.TYPE_int32

    def _mod_egg_incubator_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[25] = ProtoBase.TYPE_int32

    def _del_egg_incubator_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 25 in self._cache:
            del self._cache[25]
        if 25 in self._mods:
            del self._mods[25]
        self._buf_del(25)

    _pb_field_name_25 = "egg_incubator_id"

    egg_incubator_id = property(_get_egg_incubator_id, _set_egg_incubator_id, _del_egg_incubator_id)

    @property
    def egg_incubator_id__exists(self):
        return 25 in self._mods or self._buf_exists(25)

    @property
    def egg_incubator_id__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_egg_incubator_id(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(25)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(25)

    _pbf_finalizers.append(_finalize_egg_incubator_id)


    def _get_creation_time_ms(self):
        if 26 in self._cache:
            r = self._cache[26]
        else:
            r = self._buf_get(26, ProtoBase.TYPE_uint64, 'creation_time_ms')
            self._cache[26] = r
        return r

    def _establish_parentage_creation_time_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_creation_time_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_creation_time_ms
                v._pbf_establish_parent_callback = self._establish_parentage_creation_time_ms

    def _set_creation_time_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_creation_time_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field creation_time_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[26] = v
        self._mods[26] = ProtoBase.TYPE_uint64

    def _mod_creation_time_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[26] = ProtoBase.TYPE_uint64

    def _del_creation_time_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 26 in self._cache:
            del self._cache[26]
        if 26 in self._mods:
            del self._mods[26]
        self._buf_del(26)

    _pb_field_name_26 = "creation_time_ms"

    creation_time_ms = property(_get_creation_time_ms, _set_creation_time_ms, _del_creation_time_ms)

    @property
    def creation_time_ms__exists(self):
        return 26 in self._mods or self._buf_exists(26)

    @property
    def creation_time_ms__type(self):
        return ProtoBase.TYPE_uint64

    def _finalize_creation_time_ms(cls):
        if is_string(ProtoBase.TYPE_uint64):
            cls._pbf_strings.append(26)
        elif _PB_type(ProtoBase.TYPE_uint64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_uint64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_uint64.pb_subtype):
                cls._pbf_strings.append(26)

    _pbf_finalizers.append(_finalize_creation_time_ms)


    def _get_num_upgrades(self):
        if 27 in self._cache:
            r = self._cache[27]
        else:
            r = self._buf_get(27, ProtoBase.TYPE_int32, 'num_upgrades')
            self._cache[27] = r
        return r

    def _establish_parentage_num_upgrades(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_num_upgrades), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_num_upgrades
                v._pbf_establish_parent_callback = self._establish_parentage_num_upgrades

    def _set_num_upgrades(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_num_upgrades(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field num_upgrades"
            raise ProtoValueError(list_assign_error)
        self._cache[27] = v
        self._mods[27] = ProtoBase.TYPE_int32

    def _mod_num_upgrades(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[27] = ProtoBase.TYPE_int32

    def _del_num_upgrades(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 27 in self._cache:
            del self._cache[27]
        if 27 in self._mods:
            del self._mods[27]
        self._buf_del(27)

    _pb_field_name_27 = "num_upgrades"

    num_upgrades = property(_get_num_upgrades, _set_num_upgrades, _del_num_upgrades)

    @property
    def num_upgrades__exists(self):
        return 27 in self._mods or self._buf_exists(27)

    @property
    def num_upgrades__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_num_upgrades(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(27)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(27)

    _pbf_finalizers.append(_finalize_num_upgrades)


    def _get_additional_cp_multiplier(self):
        if 28 in self._cache:
            r = self._cache[28]
        else:
            r = self._buf_get(28, ProtoBase.TYPE_int32, 'additional_cp_multiplier')
            self._cache[28] = r
        return r

    def _establish_parentage_additional_cp_multiplier(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_additional_cp_multiplier), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_additional_cp_multiplier
                v._pbf_establish_parent_callback = self._establish_parentage_additional_cp_multiplier

    def _set_additional_cp_multiplier(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_additional_cp_multiplier(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field additional_cp_multiplier"
            raise ProtoValueError(list_assign_error)
        self._cache[28] = v
        self._mods[28] = ProtoBase.TYPE_int32

    def _mod_additional_cp_multiplier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[28] = ProtoBase.TYPE_int32

    def _del_additional_cp_multiplier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 28 in self._cache:
            del self._cache[28]
        if 28 in self._mods:
            del self._mods[28]
        self._buf_del(28)

    _pb_field_name_28 = "additional_cp_multiplier"

    additional_cp_multiplier = property(_get_additional_cp_multiplier, _set_additional_cp_multiplier, _del_additional_cp_multiplier)

    @property
    def additional_cp_multiplier__exists(self):
        return 28 in self._mods or self._buf_exists(28)

    @property
    def additional_cp_multiplier__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_additional_cp_multiplier(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(28)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(28)

    _pbf_finalizers.append(_finalize_additional_cp_multiplier)


    def _get_favorite(self):
        if 29 in self._cache:
            r = self._cache[29]
        else:
            r = self._buf_get(29, ProtoBase.TYPE_int32, 'favorite')
            self._cache[29] = r
        return r

    def _establish_parentage_favorite(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_favorite), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_favorite
                v._pbf_establish_parent_callback = self._establish_parentage_favorite

    def _set_favorite(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_favorite(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field favorite"
            raise ProtoValueError(list_assign_error)
        self._cache[29] = v
        self._mods[29] = ProtoBase.TYPE_int32

    def _mod_favorite(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[29] = ProtoBase.TYPE_int32

    def _del_favorite(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 29 in self._cache:
            del self._cache[29]
        if 29 in self._mods:
            del self._mods[29]
        self._buf_del(29)

    _pb_field_name_29 = "favorite"

    favorite = property(_get_favorite, _set_favorite, _del_favorite)

    @property
    def favorite__exists(self):
        return 29 in self._mods or self._buf_exists(29)

    @property
    def favorite__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_favorite(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(29)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(29)

    _pbf_finalizers.append(_finalize_favorite)


    def _get_nickname(self):
        if 30 in self._cache:
            r = self._cache[30]
        else:
            r = self._buf_get(30, ProtoBase.TYPE_string, 'nickname')
            self._cache[30] = r
        return r

    def _establish_parentage_nickname(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_nickname), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_nickname
                v._pbf_establish_parent_callback = self._establish_parentage_nickname

    def _set_nickname(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_nickname(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field nickname"
            raise ProtoValueError(list_assign_error)
        self._cache[30] = v
        self._mods[30] = ProtoBase.TYPE_string

    def _mod_nickname(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[30] = ProtoBase.TYPE_string

    def _del_nickname(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 30 in self._cache:
            del self._cache[30]
        if 30 in self._mods:
            del self._mods[30]
        self._buf_del(30)

    _pb_field_name_30 = "nickname"

    nickname = property(_get_nickname, _set_nickname, _del_nickname)

    @property
    def nickname__exists(self):
        return 30 in self._mods or self._buf_exists(30)

    @property
    def nickname__type(self):
        return ProtoBase.TYPE_string

    def _finalize_nickname(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(30)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(30)

    _pbf_finalizers.append(_finalize_nickname)


    def _get_from_fort(self):
        if 31 in self._cache:
            r = self._cache[31]
        else:
            r = self._buf_get(31, ProtoBase.TYPE_int32, 'from_fort')
            self._cache[31] = r
        return r

    def _establish_parentage_from_fort(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_from_fort), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_from_fort
                v._pbf_establish_parent_callback = self._establish_parentage_from_fort

    def _set_from_fort(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_from_fort(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field from_fort"
            raise ProtoValueError(list_assign_error)
        self._cache[31] = v
        self._mods[31] = ProtoBase.TYPE_int32

    def _mod_from_fort(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[31] = ProtoBase.TYPE_int32

    def _del_from_fort(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 31 in self._cache:
            del self._cache[31]
        if 31 in self._mods:
            del self._mods[31]
        self._buf_del(31)

    _pb_field_name_31 = "from_fort"

    from_fort = property(_get_from_fort, _set_from_fort, _del_from_fort)

    @property
    def from_fort__exists(self):
        return 31 in self._mods or self._buf_exists(31)

    @property
    def from_fort__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_from_fort(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(31)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(31)

    _pbf_finalizers.append(_finalize_from_fort)


TYPE_PokemonData = PokemonData
_PB_finalizers.append('PokemonData')

class MapPokemon(ProtoBase):
    _required = []
    _field_map = {'pokemon_id': 3, 'spawnpoint_id': 1, 'longitude': 6, 'expiration_timestamp_ms': 4, 'latitude': 5, 'encounter_id': 2}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['spawnpoint_id', 'encounter_id', 'pokemon_id', 'expiration_timestamp_ms', 'latitude', 'longitude']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_spawnpoint_id(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_string, 'spawnpoint_id')
            self._cache[1] = r
        return r

    def _establish_parentage_spawnpoint_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_spawnpoint_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_spawnpoint_id
                v._pbf_establish_parent_callback = self._establish_parentage_spawnpoint_id

    def _set_spawnpoint_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_spawnpoint_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field spawnpoint_id"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_string

    def _mod_spawnpoint_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_string

    def _del_spawnpoint_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "spawnpoint_id"

    spawnpoint_id = property(_get_spawnpoint_id, _set_spawnpoint_id, _del_spawnpoint_id)

    @property
    def spawnpoint_id__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def spawnpoint_id__type(self):
        return ProtoBase.TYPE_string

    def _finalize_spawnpoint_id(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_spawnpoint_id)


    def _get_encounter_id(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_fixed64, 'encounter_id')
            self._cache[2] = r
        return r

    def _establish_parentage_encounter_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_encounter_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_encounter_id
                v._pbf_establish_parent_callback = self._establish_parentage_encounter_id

    def _set_encounter_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_encounter_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field encounter_id"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_fixed64

    def _mod_encounter_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_fixed64

    def _del_encounter_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "encounter_id"

    encounter_id = property(_get_encounter_id, _set_encounter_id, _del_encounter_id)

    @property
    def encounter_id__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def encounter_id__type(self):
        return ProtoBase.TYPE_fixed64

    def _finalize_encounter_id(cls):
        if is_string(ProtoBase.TYPE_fixed64):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_fixed64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_fixed64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_fixed64.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_encounter_id)


    def _get_pokemon_id(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, RpcEnum_palm.TYPE_PokemonId, 'pokemon_id')
            self._cache[3] = r
        return r

    def _establish_parentage_pokemon_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokemon_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokemon_id
                v._pbf_establish_parent_callback = self._establish_parentage_pokemon_id

    def _set_pokemon_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokemon_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokemon_id"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = RpcEnum_palm.TYPE_PokemonId

    def _mod_pokemon_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = RpcEnum_palm.TYPE_PokemonId

    def _del_pokemon_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "pokemon_id"

    pokemon_id = property(_get_pokemon_id, _set_pokemon_id, _del_pokemon_id)

    @property
    def pokemon_id__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def pokemon_id__type(self):
        return RpcEnum_palm.TYPE_PokemonId

    def _finalize_pokemon_id(cls):
        if is_string(RpcEnum_palm.TYPE_PokemonId):
            cls._pbf_strings.append(3)
        elif _PB_type(RpcEnum_palm.TYPE_PokemonId) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_PokemonId, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_PokemonId.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_pokemon_id)


    def _get_expiration_timestamp_ms(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, ProtoBase.TYPE_int64, 'expiration_timestamp_ms')
            self._cache[4] = r
        return r

    def _establish_parentage_expiration_timestamp_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_expiration_timestamp_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_expiration_timestamp_ms
                v._pbf_establish_parent_callback = self._establish_parentage_expiration_timestamp_ms

    def _set_expiration_timestamp_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_expiration_timestamp_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field expiration_timestamp_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = ProtoBase.TYPE_int64

    def _mod_expiration_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = ProtoBase.TYPE_int64

    def _del_expiration_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "expiration_timestamp_ms"

    expiration_timestamp_ms = property(_get_expiration_timestamp_ms, _set_expiration_timestamp_ms, _del_expiration_timestamp_ms)

    @property
    def expiration_timestamp_ms__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def expiration_timestamp_ms__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_expiration_timestamp_ms(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(4)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_expiration_timestamp_ms)


    def _get_latitude(self):
        if 5 in self._cache:
            r = self._cache[5]
        else:
            r = self._buf_get(5, ProtoBase.TYPE_double, 'latitude')
            self._cache[5] = r
        return r

    def _establish_parentage_latitude(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_latitude), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_latitude
                v._pbf_establish_parent_callback = self._establish_parentage_latitude

    def _set_latitude(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_latitude(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field latitude"
            raise ProtoValueError(list_assign_error)
        self._cache[5] = v
        self._mods[5] = ProtoBase.TYPE_double

    def _mod_latitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[5] = ProtoBase.TYPE_double

    def _del_latitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 5 in self._cache:
            del self._cache[5]
        if 5 in self._mods:
            del self._mods[5]
        self._buf_del(5)

    _pb_field_name_5 = "latitude"

    latitude = property(_get_latitude, _set_latitude, _del_latitude)

    @property
    def latitude__exists(self):
        return 5 in self._mods or self._buf_exists(5)

    @property
    def latitude__type(self):
        return ProtoBase.TYPE_double

    def _finalize_latitude(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(5)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(5)

    _pbf_finalizers.append(_finalize_latitude)


    def _get_longitude(self):
        if 6 in self._cache:
            r = self._cache[6]
        else:
            r = self._buf_get(6, ProtoBase.TYPE_double, 'longitude')
            self._cache[6] = r
        return r

    def _establish_parentage_longitude(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_longitude), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_longitude
                v._pbf_establish_parent_callback = self._establish_parentage_longitude

    def _set_longitude(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_longitude(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field longitude"
            raise ProtoValueError(list_assign_error)
        self._cache[6] = v
        self._mods[6] = ProtoBase.TYPE_double

    def _mod_longitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[6] = ProtoBase.TYPE_double

    def _del_longitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 6 in self._cache:
            del self._cache[6]
        if 6 in self._mods:
            del self._mods[6]
        self._buf_del(6)

    _pb_field_name_6 = "longitude"

    longitude = property(_get_longitude, _set_longitude, _del_longitude)

    @property
    def longitude__exists(self):
        return 6 in self._mods or self._buf_exists(6)

    @property
    def longitude__type(self):
        return ProtoBase.TYPE_double

    def _finalize_longitude(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(6)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(6)

    _pbf_finalizers.append(_finalize_longitude)


TYPE_MapPokemon = MapPokemon
_PB_finalizers.append('MapPokemon')

class NearbyPokemon(ProtoBase):
    _required = []
    _field_map = {'distance_in_meters': 2, 'encounter_id': 3, 'pokemon_id': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['pokemon_id', 'distance_in_meters', 'encounter_id']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_pokemon_id(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, RpcEnum_palm.TYPE_PokemonId, 'pokemon_id')
            self._cache[1] = r
        return r

    def _establish_parentage_pokemon_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokemon_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokemon_id
                v._pbf_establish_parent_callback = self._establish_parentage_pokemon_id

    def _set_pokemon_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokemon_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokemon_id"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = RpcEnum_palm.TYPE_PokemonId

    def _mod_pokemon_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = RpcEnum_palm.TYPE_PokemonId

    def _del_pokemon_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "pokemon_id"

    pokemon_id = property(_get_pokemon_id, _set_pokemon_id, _del_pokemon_id)

    @property
    def pokemon_id__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def pokemon_id__type(self):
        return RpcEnum_palm.TYPE_PokemonId

    def _finalize_pokemon_id(cls):
        if is_string(RpcEnum_palm.TYPE_PokemonId):
            cls._pbf_strings.append(1)
        elif _PB_type(RpcEnum_palm.TYPE_PokemonId) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_PokemonId, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_PokemonId.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_pokemon_id)


    def _get_distance_in_meters(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_float, 'distance_in_meters')
            self._cache[2] = r
        return r

    def _establish_parentage_distance_in_meters(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_distance_in_meters), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_distance_in_meters
                v._pbf_establish_parent_callback = self._establish_parentage_distance_in_meters

    def _set_distance_in_meters(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_distance_in_meters(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field distance_in_meters"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_float

    def _mod_distance_in_meters(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_float

    def _del_distance_in_meters(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "distance_in_meters"

    distance_in_meters = property(_get_distance_in_meters, _set_distance_in_meters, _del_distance_in_meters)

    @property
    def distance_in_meters__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def distance_in_meters__type(self):
        return ProtoBase.TYPE_float

    def _finalize_distance_in_meters(cls):
        if is_string(ProtoBase.TYPE_float):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_float) is _PB_type:
            assert issubclass(ProtoBase.TYPE_float, RepeatedSequence)
            if is_string(ProtoBase.TYPE_float.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_distance_in_meters)


    def _get_encounter_id(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_fixed64, 'encounter_id')
            self._cache[3] = r
        return r

    def _establish_parentage_encounter_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_encounter_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_encounter_id
                v._pbf_establish_parent_callback = self._establish_parentage_encounter_id

    def _set_encounter_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_encounter_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field encounter_id"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_fixed64

    def _mod_encounter_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_fixed64

    def _del_encounter_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "encounter_id"

    encounter_id = property(_get_encounter_id, _set_encounter_id, _del_encounter_id)

    @property
    def encounter_id__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def encounter_id__type(self):
        return ProtoBase.TYPE_fixed64

    def _finalize_encounter_id(cls):
        if is_string(ProtoBase.TYPE_fixed64):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_fixed64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_fixed64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_fixed64.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_encounter_id)


TYPE_NearbyPokemon = NearbyPokemon
_PB_finalizers.append('NearbyPokemon')

class DownloadSettingsResponse(ProtoBase):
    _required = []
    _field_map = {'settings': 3, 'hash': 2, 'error': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['error', 'hash', 'settings']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_error(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_string, 'error')
            self._cache[1] = r
        return r

    def _establish_parentage_error(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_error), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_error
                v._pbf_establish_parent_callback = self._establish_parentage_error

    def _set_error(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_error(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field error"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_string

    def _mod_error(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_string

    def _del_error(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "error"

    error = property(_get_error, _set_error, _del_error)

    @property
    def error__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def error__type(self):
        return ProtoBase.TYPE_string

    def _finalize_error(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_error)


    def _get_hash(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_string, 'hash')
            self._cache[2] = r
        return r

    def _establish_parentage_hash(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_hash), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_hash
                v._pbf_establish_parent_callback = self._establish_parentage_hash

    def _set_hash(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_hash(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field hash"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_string

    def _mod_hash(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_string

    def _del_hash(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "hash"

    hash = property(_get_hash, _set_hash, _del_hash)

    @property
    def hash__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def hash__type(self):
        return ProtoBase.TYPE_string

    def _finalize_hash(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_hash)


    def _get_settings(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, TYPE_GlobalSettings, 'settings')
            self._cache[3] = r
        return r

    def _establish_parentage_settings(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_settings), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_settings
                v._pbf_establish_parent_callback = self._establish_parentage_settings

    def _set_settings(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_settings(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field settings"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = TYPE_GlobalSettings

    def _mod_settings(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = TYPE_GlobalSettings

    def _del_settings(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "settings"

    settings = property(_get_settings, _set_settings, _del_settings)

    @property
    def settings__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def settings__type(self):
        return TYPE_GlobalSettings

    def _finalize_settings(cls):
        if is_string(TYPE_GlobalSettings):
            cls._pbf_strings.append(3)
        elif _PB_type(TYPE_GlobalSettings) is _PB_type:
            assert issubclass(TYPE_GlobalSettings, RepeatedSequence)
            if is_string(TYPE_GlobalSettings.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_settings)


TYPE_DownloadSettingsResponse = DownloadSettingsResponse
_PB_finalizers.append('DownloadSettingsResponse')

class GlobalSettings(ProtoBase):
    _required = []
    _field_map = {'fort_settings': 2, 'level_settings': 4, 'inventory_settings': 5, 'map_settings': 3, 'minimum_client_version': 6}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['fort_settings', 'map_settings', 'level_settings', 'inventory_settings', 'minimum_client_version']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_fort_settings(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, TYPE_FortSettings, 'fort_settings')
            self._cache[2] = r
        return r

    def _establish_parentage_fort_settings(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_fort_settings), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_fort_settings
                v._pbf_establish_parent_callback = self._establish_parentage_fort_settings

    def _set_fort_settings(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_fort_settings(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field fort_settings"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = TYPE_FortSettings

    def _mod_fort_settings(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = TYPE_FortSettings

    def _del_fort_settings(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "fort_settings"

    fort_settings = property(_get_fort_settings, _set_fort_settings, _del_fort_settings)

    @property
    def fort_settings__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def fort_settings__type(self):
        return TYPE_FortSettings

    def _finalize_fort_settings(cls):
        if is_string(TYPE_FortSettings):
            cls._pbf_strings.append(2)
        elif _PB_type(TYPE_FortSettings) is _PB_type:
            assert issubclass(TYPE_FortSettings, RepeatedSequence)
            if is_string(TYPE_FortSettings.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_fort_settings)


    def _get_map_settings(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, TYPE_MapSettings, 'map_settings')
            self._cache[3] = r
        return r

    def _establish_parentage_map_settings(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_map_settings), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_map_settings
                v._pbf_establish_parent_callback = self._establish_parentage_map_settings

    def _set_map_settings(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_map_settings(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field map_settings"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = TYPE_MapSettings

    def _mod_map_settings(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = TYPE_MapSettings

    def _del_map_settings(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "map_settings"

    map_settings = property(_get_map_settings, _set_map_settings, _del_map_settings)

    @property
    def map_settings__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def map_settings__type(self):
        return TYPE_MapSettings

    def _finalize_map_settings(cls):
        if is_string(TYPE_MapSettings):
            cls._pbf_strings.append(3)
        elif _PB_type(TYPE_MapSettings) is _PB_type:
            assert issubclass(TYPE_MapSettings, RepeatedSequence)
            if is_string(TYPE_MapSettings.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_map_settings)


    def _get_level_settings(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, TYPE_LevelSettings, 'level_settings')
            self._cache[4] = r
        return r

    def _establish_parentage_level_settings(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_level_settings), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_level_settings
                v._pbf_establish_parent_callback = self._establish_parentage_level_settings

    def _set_level_settings(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_level_settings(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field level_settings"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = TYPE_LevelSettings

    def _mod_level_settings(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = TYPE_LevelSettings

    def _del_level_settings(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "level_settings"

    level_settings = property(_get_level_settings, _set_level_settings, _del_level_settings)

    @property
    def level_settings__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def level_settings__type(self):
        return TYPE_LevelSettings

    def _finalize_level_settings(cls):
        if is_string(TYPE_LevelSettings):
            cls._pbf_strings.append(4)
        elif _PB_type(TYPE_LevelSettings) is _PB_type:
            assert issubclass(TYPE_LevelSettings, RepeatedSequence)
            if is_string(TYPE_LevelSettings.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_level_settings)


    def _get_inventory_settings(self):
        if 5 in self._cache:
            r = self._cache[5]
        else:
            r = self._buf_get(5, TYPE_InventorySettings, 'inventory_settings')
            self._cache[5] = r
        return r

    def _establish_parentage_inventory_settings(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_inventory_settings), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_inventory_settings
                v._pbf_establish_parent_callback = self._establish_parentage_inventory_settings

    def _set_inventory_settings(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_inventory_settings(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field inventory_settings"
            raise ProtoValueError(list_assign_error)
        self._cache[5] = v
        self._mods[5] = TYPE_InventorySettings

    def _mod_inventory_settings(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[5] = TYPE_InventorySettings

    def _del_inventory_settings(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 5 in self._cache:
            del self._cache[5]
        if 5 in self._mods:
            del self._mods[5]
        self._buf_del(5)

    _pb_field_name_5 = "inventory_settings"

    inventory_settings = property(_get_inventory_settings, _set_inventory_settings, _del_inventory_settings)

    @property
    def inventory_settings__exists(self):
        return 5 in self._mods or self._buf_exists(5)

    @property
    def inventory_settings__type(self):
        return TYPE_InventorySettings

    def _finalize_inventory_settings(cls):
        if is_string(TYPE_InventorySettings):
            cls._pbf_strings.append(5)
        elif _PB_type(TYPE_InventorySettings) is _PB_type:
            assert issubclass(TYPE_InventorySettings, RepeatedSequence)
            if is_string(TYPE_InventorySettings.pb_subtype):
                cls._pbf_strings.append(5)

    _pbf_finalizers.append(_finalize_inventory_settings)


    def _get_minimum_client_version(self):
        if 6 in self._cache:
            r = self._cache[6]
        else:
            r = self._buf_get(6, ProtoBase.TYPE_string, 'minimum_client_version')
            self._cache[6] = r
        return r

    def _establish_parentage_minimum_client_version(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_minimum_client_version), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_minimum_client_version
                v._pbf_establish_parent_callback = self._establish_parentage_minimum_client_version

    def _set_minimum_client_version(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_minimum_client_version(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field minimum_client_version"
            raise ProtoValueError(list_assign_error)
        self._cache[6] = v
        self._mods[6] = ProtoBase.TYPE_string

    def _mod_minimum_client_version(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[6] = ProtoBase.TYPE_string

    def _del_minimum_client_version(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 6 in self._cache:
            del self._cache[6]
        if 6 in self._mods:
            del self._mods[6]
        self._buf_del(6)

    _pb_field_name_6 = "minimum_client_version"

    minimum_client_version = property(_get_minimum_client_version, _set_minimum_client_version, _del_minimum_client_version)

    @property
    def minimum_client_version__exists(self):
        return 6 in self._mods or self._buf_exists(6)

    @property
    def minimum_client_version__type(self):
        return ProtoBase.TYPE_string

    def _finalize_minimum_client_version(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(6)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(6)

    _pbf_finalizers.append(_finalize_minimum_client_version)


TYPE_GlobalSettings = GlobalSettings
_PB_finalizers.append('GlobalSettings')

class FortSettings(ProtoBase):
    _required = []
    _field_map = {'deploy_attack_multiplier': 5, 'max_player_deployed_pokemon': 3, 'max_total_deployed_pokemon': 2, 'far_interaction_range_meters': 6, 'deploy_stamina_multiplier': 4, 'interaction_range_meters': 1}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['interaction_range_meters', 'max_total_deployed_pokemon', 'max_player_deployed_pokemon', 'deploy_stamina_multiplier', 'deploy_attack_multiplier', 'far_interaction_range_meters']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_interaction_range_meters(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_double, 'interaction_range_meters')
            self._cache[1] = r
        return r

    def _establish_parentage_interaction_range_meters(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_interaction_range_meters), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_interaction_range_meters
                v._pbf_establish_parent_callback = self._establish_parentage_interaction_range_meters

    def _set_interaction_range_meters(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_interaction_range_meters(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field interaction_range_meters"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_double

    def _mod_interaction_range_meters(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_double

    def _del_interaction_range_meters(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "interaction_range_meters"

    interaction_range_meters = property(_get_interaction_range_meters, _set_interaction_range_meters, _del_interaction_range_meters)

    @property
    def interaction_range_meters__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def interaction_range_meters__type(self):
        return ProtoBase.TYPE_double

    def _finalize_interaction_range_meters(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_interaction_range_meters)


    def _get_max_total_deployed_pokemon(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int32, 'max_total_deployed_pokemon')
            self._cache[2] = r
        return r

    def _establish_parentage_max_total_deployed_pokemon(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_max_total_deployed_pokemon), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_max_total_deployed_pokemon
                v._pbf_establish_parent_callback = self._establish_parentage_max_total_deployed_pokemon

    def _set_max_total_deployed_pokemon(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_max_total_deployed_pokemon(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field max_total_deployed_pokemon"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_int32

    def _mod_max_total_deployed_pokemon(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int32

    def _del_max_total_deployed_pokemon(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "max_total_deployed_pokemon"

    max_total_deployed_pokemon = property(_get_max_total_deployed_pokemon, _set_max_total_deployed_pokemon, _del_max_total_deployed_pokemon)

    @property
    def max_total_deployed_pokemon__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def max_total_deployed_pokemon__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_max_total_deployed_pokemon(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_max_total_deployed_pokemon)


    def _get_max_player_deployed_pokemon(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_int32, 'max_player_deployed_pokemon')
            self._cache[3] = r
        return r

    def _establish_parentage_max_player_deployed_pokemon(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_max_player_deployed_pokemon), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_max_player_deployed_pokemon
                v._pbf_establish_parent_callback = self._establish_parentage_max_player_deployed_pokemon

    def _set_max_player_deployed_pokemon(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_max_player_deployed_pokemon(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field max_player_deployed_pokemon"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_int32

    def _mod_max_player_deployed_pokemon(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_int32

    def _del_max_player_deployed_pokemon(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "max_player_deployed_pokemon"

    max_player_deployed_pokemon = property(_get_max_player_deployed_pokemon, _set_max_player_deployed_pokemon, _del_max_player_deployed_pokemon)

    @property
    def max_player_deployed_pokemon__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def max_player_deployed_pokemon__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_max_player_deployed_pokemon(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_max_player_deployed_pokemon)


    def _get_deploy_stamina_multiplier(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, ProtoBase.TYPE_double, 'deploy_stamina_multiplier')
            self._cache[4] = r
        return r

    def _establish_parentage_deploy_stamina_multiplier(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_deploy_stamina_multiplier), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_deploy_stamina_multiplier
                v._pbf_establish_parent_callback = self._establish_parentage_deploy_stamina_multiplier

    def _set_deploy_stamina_multiplier(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_deploy_stamina_multiplier(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field deploy_stamina_multiplier"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = ProtoBase.TYPE_double

    def _mod_deploy_stamina_multiplier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = ProtoBase.TYPE_double

    def _del_deploy_stamina_multiplier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "deploy_stamina_multiplier"

    deploy_stamina_multiplier = property(_get_deploy_stamina_multiplier, _set_deploy_stamina_multiplier, _del_deploy_stamina_multiplier)

    @property
    def deploy_stamina_multiplier__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def deploy_stamina_multiplier__type(self):
        return ProtoBase.TYPE_double

    def _finalize_deploy_stamina_multiplier(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(4)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_deploy_stamina_multiplier)


    def _get_deploy_attack_multiplier(self):
        if 5 in self._cache:
            r = self._cache[5]
        else:
            r = self._buf_get(5, ProtoBase.TYPE_double, 'deploy_attack_multiplier')
            self._cache[5] = r
        return r

    def _establish_parentage_deploy_attack_multiplier(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_deploy_attack_multiplier), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_deploy_attack_multiplier
                v._pbf_establish_parent_callback = self._establish_parentage_deploy_attack_multiplier

    def _set_deploy_attack_multiplier(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_deploy_attack_multiplier(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field deploy_attack_multiplier"
            raise ProtoValueError(list_assign_error)
        self._cache[5] = v
        self._mods[5] = ProtoBase.TYPE_double

    def _mod_deploy_attack_multiplier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[5] = ProtoBase.TYPE_double

    def _del_deploy_attack_multiplier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 5 in self._cache:
            del self._cache[5]
        if 5 in self._mods:
            del self._mods[5]
        self._buf_del(5)

    _pb_field_name_5 = "deploy_attack_multiplier"

    deploy_attack_multiplier = property(_get_deploy_attack_multiplier, _set_deploy_attack_multiplier, _del_deploy_attack_multiplier)

    @property
    def deploy_attack_multiplier__exists(self):
        return 5 in self._mods or self._buf_exists(5)

    @property
    def deploy_attack_multiplier__type(self):
        return ProtoBase.TYPE_double

    def _finalize_deploy_attack_multiplier(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(5)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(5)

    _pbf_finalizers.append(_finalize_deploy_attack_multiplier)


    def _get_far_interaction_range_meters(self):
        if 6 in self._cache:
            r = self._cache[6]
        else:
            r = self._buf_get(6, ProtoBase.TYPE_double, 'far_interaction_range_meters')
            self._cache[6] = r
        return r

    def _establish_parentage_far_interaction_range_meters(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_far_interaction_range_meters), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_far_interaction_range_meters
                v._pbf_establish_parent_callback = self._establish_parentage_far_interaction_range_meters

    def _set_far_interaction_range_meters(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_far_interaction_range_meters(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field far_interaction_range_meters"
            raise ProtoValueError(list_assign_error)
        self._cache[6] = v
        self._mods[6] = ProtoBase.TYPE_double

    def _mod_far_interaction_range_meters(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[6] = ProtoBase.TYPE_double

    def _del_far_interaction_range_meters(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 6 in self._cache:
            del self._cache[6]
        if 6 in self._mods:
            del self._mods[6]
        self._buf_del(6)

    _pb_field_name_6 = "far_interaction_range_meters"

    far_interaction_range_meters = property(_get_far_interaction_range_meters, _set_far_interaction_range_meters, _del_far_interaction_range_meters)

    @property
    def far_interaction_range_meters__exists(self):
        return 6 in self._mods or self._buf_exists(6)

    @property
    def far_interaction_range_meters__type(self):
        return ProtoBase.TYPE_double

    def _finalize_far_interaction_range_meters(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(6)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(6)

    _pbf_finalizers.append(_finalize_far_interaction_range_meters)


TYPE_FortSettings = FortSettings
_PB_finalizers.append('FortSettings')

class MapSettings(ProtoBase):
    _required = []
    _field_map = {'get_map_objects_max_refresh_seconds': 5, 'get_map_objects_min_distance_meters': 6, 'encounter_range_meters': 3, 'poke_nav_range_meters': 2, 'pokemon_visible_range': 1, 'get_map_objects_min_refresh_seconds': 4, 'google_maps_api_key': 7}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['pokemon_visible_range', 'poke_nav_range_meters', 'encounter_range_meters', 'get_map_objects_min_refresh_seconds', 'get_map_objects_max_refresh_seconds', 'get_map_objects_min_distance_meters', 'google_maps_api_key']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_pokemon_visible_range(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_double, 'pokemon_visible_range')
            self._cache[1] = r
        return r

    def _establish_parentage_pokemon_visible_range(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_pokemon_visible_range), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_pokemon_visible_range
                v._pbf_establish_parent_callback = self._establish_parentage_pokemon_visible_range

    def _set_pokemon_visible_range(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_pokemon_visible_range(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field pokemon_visible_range"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_double

    def _mod_pokemon_visible_range(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_double

    def _del_pokemon_visible_range(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "pokemon_visible_range"

    pokemon_visible_range = property(_get_pokemon_visible_range, _set_pokemon_visible_range, _del_pokemon_visible_range)

    @property
    def pokemon_visible_range__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def pokemon_visible_range__type(self):
        return ProtoBase.TYPE_double

    def _finalize_pokemon_visible_range(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_pokemon_visible_range)


    def _get_poke_nav_range_meters(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_double, 'poke_nav_range_meters')
            self._cache[2] = r
        return r

    def _establish_parentage_poke_nav_range_meters(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_poke_nav_range_meters), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_poke_nav_range_meters
                v._pbf_establish_parent_callback = self._establish_parentage_poke_nav_range_meters

    def _set_poke_nav_range_meters(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_poke_nav_range_meters(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field poke_nav_range_meters"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_double

    def _mod_poke_nav_range_meters(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_double

    def _del_poke_nav_range_meters(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "poke_nav_range_meters"

    poke_nav_range_meters = property(_get_poke_nav_range_meters, _set_poke_nav_range_meters, _del_poke_nav_range_meters)

    @property
    def poke_nav_range_meters__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def poke_nav_range_meters__type(self):
        return ProtoBase.TYPE_double

    def _finalize_poke_nav_range_meters(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_poke_nav_range_meters)


    def _get_encounter_range_meters(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_double, 'encounter_range_meters')
            self._cache[3] = r
        return r

    def _establish_parentage_encounter_range_meters(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_encounter_range_meters), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_encounter_range_meters
                v._pbf_establish_parent_callback = self._establish_parentage_encounter_range_meters

    def _set_encounter_range_meters(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_encounter_range_meters(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field encounter_range_meters"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_double

    def _mod_encounter_range_meters(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_double

    def _del_encounter_range_meters(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "encounter_range_meters"

    encounter_range_meters = property(_get_encounter_range_meters, _set_encounter_range_meters, _del_encounter_range_meters)

    @property
    def encounter_range_meters__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def encounter_range_meters__type(self):
        return ProtoBase.TYPE_double

    def _finalize_encounter_range_meters(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_encounter_range_meters)


    def _get_get_map_objects_min_refresh_seconds(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, ProtoBase.TYPE_float, 'get_map_objects_min_refresh_seconds')
            self._cache[4] = r
        return r

    def _establish_parentage_get_map_objects_min_refresh_seconds(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_get_map_objects_min_refresh_seconds), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_get_map_objects_min_refresh_seconds
                v._pbf_establish_parent_callback = self._establish_parentage_get_map_objects_min_refresh_seconds

    def _set_get_map_objects_min_refresh_seconds(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_get_map_objects_min_refresh_seconds(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field get_map_objects_min_refresh_seconds"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = ProtoBase.TYPE_float

    def _mod_get_map_objects_min_refresh_seconds(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = ProtoBase.TYPE_float

    def _del_get_map_objects_min_refresh_seconds(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "get_map_objects_min_refresh_seconds"

    get_map_objects_min_refresh_seconds = property(_get_get_map_objects_min_refresh_seconds, _set_get_map_objects_min_refresh_seconds, _del_get_map_objects_min_refresh_seconds)

    @property
    def get_map_objects_min_refresh_seconds__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def get_map_objects_min_refresh_seconds__type(self):
        return ProtoBase.TYPE_float

    def _finalize_get_map_objects_min_refresh_seconds(cls):
        if is_string(ProtoBase.TYPE_float):
            cls._pbf_strings.append(4)
        elif _PB_type(ProtoBase.TYPE_float) is _PB_type:
            assert issubclass(ProtoBase.TYPE_float, RepeatedSequence)
            if is_string(ProtoBase.TYPE_float.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_get_map_objects_min_refresh_seconds)


    def _get_get_map_objects_max_refresh_seconds(self):
        if 5 in self._cache:
            r = self._cache[5]
        else:
            r = self._buf_get(5, ProtoBase.TYPE_float, 'get_map_objects_max_refresh_seconds')
            self._cache[5] = r
        return r

    def _establish_parentage_get_map_objects_max_refresh_seconds(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_get_map_objects_max_refresh_seconds), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_get_map_objects_max_refresh_seconds
                v._pbf_establish_parent_callback = self._establish_parentage_get_map_objects_max_refresh_seconds

    def _set_get_map_objects_max_refresh_seconds(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_get_map_objects_max_refresh_seconds(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field get_map_objects_max_refresh_seconds"
            raise ProtoValueError(list_assign_error)
        self._cache[5] = v
        self._mods[5] = ProtoBase.TYPE_float

    def _mod_get_map_objects_max_refresh_seconds(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[5] = ProtoBase.TYPE_float

    def _del_get_map_objects_max_refresh_seconds(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 5 in self._cache:
            del self._cache[5]
        if 5 in self._mods:
            del self._mods[5]
        self._buf_del(5)

    _pb_field_name_5 = "get_map_objects_max_refresh_seconds"

    get_map_objects_max_refresh_seconds = property(_get_get_map_objects_max_refresh_seconds, _set_get_map_objects_max_refresh_seconds, _del_get_map_objects_max_refresh_seconds)

    @property
    def get_map_objects_max_refresh_seconds__exists(self):
        return 5 in self._mods or self._buf_exists(5)

    @property
    def get_map_objects_max_refresh_seconds__type(self):
        return ProtoBase.TYPE_float

    def _finalize_get_map_objects_max_refresh_seconds(cls):
        if is_string(ProtoBase.TYPE_float):
            cls._pbf_strings.append(5)
        elif _PB_type(ProtoBase.TYPE_float) is _PB_type:
            assert issubclass(ProtoBase.TYPE_float, RepeatedSequence)
            if is_string(ProtoBase.TYPE_float.pb_subtype):
                cls._pbf_strings.append(5)

    _pbf_finalizers.append(_finalize_get_map_objects_max_refresh_seconds)


    def _get_get_map_objects_min_distance_meters(self):
        if 6 in self._cache:
            r = self._cache[6]
        else:
            r = self._buf_get(6, ProtoBase.TYPE_float, 'get_map_objects_min_distance_meters')
            self._cache[6] = r
        return r

    def _establish_parentage_get_map_objects_min_distance_meters(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_get_map_objects_min_distance_meters), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_get_map_objects_min_distance_meters
                v._pbf_establish_parent_callback = self._establish_parentage_get_map_objects_min_distance_meters

    def _set_get_map_objects_min_distance_meters(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_get_map_objects_min_distance_meters(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field get_map_objects_min_distance_meters"
            raise ProtoValueError(list_assign_error)
        self._cache[6] = v
        self._mods[6] = ProtoBase.TYPE_float

    def _mod_get_map_objects_min_distance_meters(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[6] = ProtoBase.TYPE_float

    def _del_get_map_objects_min_distance_meters(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 6 in self._cache:
            del self._cache[6]
        if 6 in self._mods:
            del self._mods[6]
        self._buf_del(6)

    _pb_field_name_6 = "get_map_objects_min_distance_meters"

    get_map_objects_min_distance_meters = property(_get_get_map_objects_min_distance_meters, _set_get_map_objects_min_distance_meters, _del_get_map_objects_min_distance_meters)

    @property
    def get_map_objects_min_distance_meters__exists(self):
        return 6 in self._mods or self._buf_exists(6)

    @property
    def get_map_objects_min_distance_meters__type(self):
        return ProtoBase.TYPE_float

    def _finalize_get_map_objects_min_distance_meters(cls):
        if is_string(ProtoBase.TYPE_float):
            cls._pbf_strings.append(6)
        elif _PB_type(ProtoBase.TYPE_float) is _PB_type:
            assert issubclass(ProtoBase.TYPE_float, RepeatedSequence)
            if is_string(ProtoBase.TYPE_float.pb_subtype):
                cls._pbf_strings.append(6)

    _pbf_finalizers.append(_finalize_get_map_objects_min_distance_meters)


    def _get_google_maps_api_key(self):
        if 7 in self._cache:
            r = self._cache[7]
        else:
            r = self._buf_get(7, ProtoBase.TYPE_string, 'google_maps_api_key')
            self._cache[7] = r
        return r

    def _establish_parentage_google_maps_api_key(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_google_maps_api_key), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_google_maps_api_key
                v._pbf_establish_parent_callback = self._establish_parentage_google_maps_api_key

    def _set_google_maps_api_key(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_google_maps_api_key(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field google_maps_api_key"
            raise ProtoValueError(list_assign_error)
        self._cache[7] = v
        self._mods[7] = ProtoBase.TYPE_string

    def _mod_google_maps_api_key(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[7] = ProtoBase.TYPE_string

    def _del_google_maps_api_key(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 7 in self._cache:
            del self._cache[7]
        if 7 in self._mods:
            del self._mods[7]
        self._buf_del(7)

    _pb_field_name_7 = "google_maps_api_key"

    google_maps_api_key = property(_get_google_maps_api_key, _set_google_maps_api_key, _del_google_maps_api_key)

    @property
    def google_maps_api_key__exists(self):
        return 7 in self._mods or self._buf_exists(7)

    @property
    def google_maps_api_key__type(self):
        return ProtoBase.TYPE_string

    def _finalize_google_maps_api_key(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(7)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(7)

    _pbf_finalizers.append(_finalize_google_maps_api_key)


TYPE_MapSettings = MapSettings
_PB_finalizers.append('MapSettings')

class LevelSettings(ProtoBase):
    _required = []
    _field_map = {'trainer_cp_modifier': 2, 'trainer_difficulty_modifier': 3}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['trainer_cp_modifier', 'trainer_difficulty_modifier']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_trainer_cp_modifier(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_double, 'trainer_cp_modifier')
            self._cache[2] = r
        return r

    def _establish_parentage_trainer_cp_modifier(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_trainer_cp_modifier), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_trainer_cp_modifier
                v._pbf_establish_parent_callback = self._establish_parentage_trainer_cp_modifier

    def _set_trainer_cp_modifier(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_trainer_cp_modifier(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field trainer_cp_modifier"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_double

    def _mod_trainer_cp_modifier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_double

    def _del_trainer_cp_modifier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "trainer_cp_modifier"

    trainer_cp_modifier = property(_get_trainer_cp_modifier, _set_trainer_cp_modifier, _del_trainer_cp_modifier)

    @property
    def trainer_cp_modifier__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def trainer_cp_modifier__type(self):
        return ProtoBase.TYPE_double

    def _finalize_trainer_cp_modifier(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_trainer_cp_modifier)


    def _get_trainer_difficulty_modifier(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_double, 'trainer_difficulty_modifier')
            self._cache[3] = r
        return r

    def _establish_parentage_trainer_difficulty_modifier(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_trainer_difficulty_modifier), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_trainer_difficulty_modifier
                v._pbf_establish_parent_callback = self._establish_parentage_trainer_difficulty_modifier

    def _set_trainer_difficulty_modifier(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_trainer_difficulty_modifier(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field trainer_difficulty_modifier"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_double

    def _mod_trainer_difficulty_modifier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_double

    def _del_trainer_difficulty_modifier(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "trainer_difficulty_modifier"

    trainer_difficulty_modifier = property(_get_trainer_difficulty_modifier, _set_trainer_difficulty_modifier, _del_trainer_difficulty_modifier)

    @property
    def trainer_difficulty_modifier__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def trainer_difficulty_modifier__type(self):
        return ProtoBase.TYPE_double

    def _finalize_trainer_difficulty_modifier(cls):
        if is_string(ProtoBase.TYPE_double):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_double) is _PB_type:
            assert issubclass(ProtoBase.TYPE_double, RepeatedSequence)
            if is_string(ProtoBase.TYPE_double.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_trainer_difficulty_modifier)


TYPE_LevelSettings = LevelSettings
_PB_finalizers.append('LevelSettings')

class InventorySettings(ProtoBase):
    _required = []
    _field_map = {'base_bag_items': 4, 'max_pokemon': 1, 'base_eggs': 5, 'max_bag_items': 2, 'base_pokemon': 3}
    
    def __init__(self, _pbf_buf='', _pbf_parent_callback=None, **kw):
        self._pbf_parent_callback = _pbf_parent_callback
        self._cache = {}
        self._pbf_establish_parent_callback = None
        ProtoBase.__init__(self, _pbf_buf, **kw)

    @classmethod
    def _pbf_finalize(cls):
        for c in cls._pbf_finalizers:
            c(cls)
        del cls._pbf_finalizers

    @classmethod
    def fields(cls):
        return ['max_pokemon', 'max_bag_items', 'base_pokemon', 'base_bag_items', 'base_eggs']

    def modified(self):
        return self._evermod

    def __contains__(self, item):
        try:
            return getattr(self, '%s__exists' % item)
        except AttributeError:
            return False

    _pbf_strings = []
    _pbf_finalizers = []

    def __str__(self):
        return '\n'.join('%s: %s' % (f, repr(getattr(self, '_get_%s' % f)())) for f in self.fields()
                          if getattr(self, '%s__exists' % f))

    def _get_max_pokemon(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_int32, 'max_pokemon')
            self._cache[1] = r
        return r

    def _establish_parentage_max_pokemon(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_max_pokemon), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_max_pokemon
                v._pbf_establish_parent_callback = self._establish_parentage_max_pokemon

    def _set_max_pokemon(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_max_pokemon(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field max_pokemon"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_int32

    def _mod_max_pokemon(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_int32

    def _del_max_pokemon(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "max_pokemon"

    max_pokemon = property(_get_max_pokemon, _set_max_pokemon, _del_max_pokemon)

    @property
    def max_pokemon__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def max_pokemon__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_max_pokemon(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_max_pokemon)


    def _get_max_bag_items(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int32, 'max_bag_items')
            self._cache[2] = r
        return r

    def _establish_parentage_max_bag_items(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_max_bag_items), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_max_bag_items
                v._pbf_establish_parent_callback = self._establish_parentage_max_bag_items

    def _set_max_bag_items(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_max_bag_items(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field max_bag_items"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_int32

    def _mod_max_bag_items(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int32

    def _del_max_bag_items(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "max_bag_items"

    max_bag_items = property(_get_max_bag_items, _set_max_bag_items, _del_max_bag_items)

    @property
    def max_bag_items__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def max_bag_items__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_max_bag_items(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_max_bag_items)


    def _get_base_pokemon(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_int32, 'base_pokemon')
            self._cache[3] = r
        return r

    def _establish_parentage_base_pokemon(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_base_pokemon), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_base_pokemon
                v._pbf_establish_parent_callback = self._establish_parentage_base_pokemon

    def _set_base_pokemon(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_base_pokemon(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field base_pokemon"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_int32

    def _mod_base_pokemon(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_int32

    def _del_base_pokemon(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "base_pokemon"

    base_pokemon = property(_get_base_pokemon, _set_base_pokemon, _del_base_pokemon)

    @property
    def base_pokemon__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def base_pokemon__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_base_pokemon(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_base_pokemon)


    def _get_base_bag_items(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, ProtoBase.TYPE_int32, 'base_bag_items')
            self._cache[4] = r
        return r

    def _establish_parentage_base_bag_items(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_base_bag_items), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_base_bag_items
                v._pbf_establish_parent_callback = self._establish_parentage_base_bag_items

    def _set_base_bag_items(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_base_bag_items(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field base_bag_items"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = ProtoBase.TYPE_int32

    def _mod_base_bag_items(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = ProtoBase.TYPE_int32

    def _del_base_bag_items(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "base_bag_items"

    base_bag_items = property(_get_base_bag_items, _set_base_bag_items, _del_base_bag_items)

    @property
    def base_bag_items__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def base_bag_items__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_base_bag_items(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(4)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_base_bag_items)


    def _get_base_eggs(self):
        if 5 in self._cache:
            r = self._cache[5]
        else:
            r = self._buf_get(5, ProtoBase.TYPE_int32, 'base_eggs')
            self._cache[5] = r
        return r

    def _establish_parentage_base_eggs(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_base_eggs), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_base_eggs
                v._pbf_establish_parent_callback = self._establish_parentage_base_eggs

    def _set_base_eggs(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_base_eggs(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field base_eggs"
            raise ProtoValueError(list_assign_error)
        self._cache[5] = v
        self._mods[5] = ProtoBase.TYPE_int32

    def _mod_base_eggs(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[5] = ProtoBase.TYPE_int32

    def _del_base_eggs(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 5 in self._cache:
            del self._cache[5]
        if 5 in self._mods:
            del self._mods[5]
        self._buf_del(5)

    _pb_field_name_5 = "base_eggs"

    base_eggs = property(_get_base_eggs, _set_base_eggs, _del_base_eggs)

    @property
    def base_eggs__exists(self):
        return 5 in self._mods or self._buf_exists(5)

    @property
    def base_eggs__type(self):
        return ProtoBase.TYPE_int32

    def _finalize_base_eggs(cls):
        if is_string(ProtoBase.TYPE_int32):
            cls._pbf_strings.append(5)
        elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int32.pb_subtype):
                cls._pbf_strings.append(5)

    _pbf_finalizers.append(_finalize_base_eggs)


TYPE_InventorySettings = InventorySettings
_PB_finalizers.append('InventorySettings')


for cname in _PB_finalizers:
    eval(cname)._pbf_finalize()

del _PB_finalizers
