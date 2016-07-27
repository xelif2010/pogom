from palm.palm import ProtoBase, is_string, RepeatedSequence, ProtoValueError

_PB_type = type
_PB_finalizers = []

import RpcEnum_palm

class Request(ProtoBase):
    _required = [1]
    _field_map = {'direction': 1, 'rpc_id': 3, 'altitude': 9, 'auth_ticket': 11, 'longitude': 8, 'unknown6': 6, 'auth': 10, 'latitude': 7, 'requests': 4, 'unknown12': 12}
    
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
        return ['direction', 'rpc_id', 'requests', 'unknown6', 'latitude', 'longitude', 'altitude', 'auth', 'auth_ticket', 'unknown12']

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
    
    class Requests(ProtoBase):
        _required = [1]
        _field_map = {'type': 1, 'parameters': 2}
        
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
            return ['type', 'parameters']
    
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
                r = self._buf_get(1, RpcEnum_palm.TYPE_RequestMethod, 'type')
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
            self._mods[1] = RpcEnum_palm.TYPE_RequestMethod
    
        def _mod_type(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            self._mods[1] = RpcEnum_palm.TYPE_RequestMethod
    
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
            return RpcEnum_palm.TYPE_RequestMethod
    
        def _finalize_type(cls):
            if is_string(RpcEnum_palm.TYPE_RequestMethod):
                cls._pbf_strings.append(1)
            elif _PB_type(RpcEnum_palm.TYPE_RequestMethod) is _PB_type:
                assert issubclass(RpcEnum_palm.TYPE_RequestMethod, RepeatedSequence)
                if is_string(RpcEnum_palm.TYPE_RequestMethod.pb_subtype):
                    cls._pbf_strings.append(1)
    
        _pbf_finalizers.append(_finalize_type)
    
        
        def _get_parameters(self):
            if 2 in self._cache:
                r = self._cache[2]
            else:
                r = self._buf_get(2, ProtoBase.TYPE_bytes, 'parameters')
                self._cache[2] = r
            return r
    
        def _establish_parentage_parameters(self, v):
            if isinstance(v, (ProtoBase, RepeatedSequence)):
                if v._pbf_parent_callback:
                    assert (v._pbf_parent_callback == self._mod_parameters), "subobjects can only have one parent--use copy()?"
                else:
                    v._pbf_parent_callback = self._mod_parameters
                    v._pbf_establish_parent_callback = self._establish_parentage_parameters
    
        def _set_parameters(self, v, modifying=True):
            self._evermod = modifying or self._evermod
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            if isinstance(v, (ProtoBase, RepeatedSequence)):
                self._establish_parentage_parameters(v)
            elif isinstance(v, list):
                list_assign_error = "Can't assign list to repeated field parameters"
                raise ProtoValueError(list_assign_error)
            self._cache[2] = v
            self._mods[2] = ProtoBase.TYPE_bytes
    
        def _mod_parameters(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            self._mods[2] = ProtoBase.TYPE_bytes
    
        def _del_parameters(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            if 2 in self._cache:
                del self._cache[2]
            if 2 in self._mods:
                del self._mods[2]
            self._buf_del(2)
    
        _pb_field_name_2 = "parameters"
    
        parameters = property(_get_parameters, _set_parameters, _del_parameters)
    
        @property
        def parameters__exists(self):
            return 2 in self._mods or self._buf_exists(2)
    
        @property
        def parameters__type(self):
            return ProtoBase.TYPE_bytes
    
        def _finalize_parameters(cls):
            if is_string(ProtoBase.TYPE_bytes):
                cls._pbf_strings.append(2)
            elif _PB_type(ProtoBase.TYPE_bytes) is _PB_type:
                assert issubclass(ProtoBase.TYPE_bytes, RepeatedSequence)
                if is_string(ProtoBase.TYPE_bytes.pb_subtype):
                    cls._pbf_strings.append(2)
    
        _pbf_finalizers.append(_finalize_parameters)
    
        
    TYPE_Requests = Requests
    _PB_finalizers.append('Request.Requests')
    
    TYPE_Requests = Requests
    
    class AuthInfo(ProtoBase):
        _required = [1, 2]
        _field_map = {'token': 2, 'provider': 1}
        
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
            return ['provider', 'token']
    
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
            
        class JWT(ProtoBase):
            _required = [1, 2]
            _field_map = {'unknown13': 2, 'contents': 1}
            
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
                return ['contents', 'unknown13']
        
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
                
            def _get_contents(self):
                if 1 in self._cache:
                    r = self._cache[1]
                else:
                    r = self._buf_get(1, ProtoBase.TYPE_string, 'contents')
                    self._cache[1] = r
                return r
        
            def _establish_parentage_contents(self, v):
                if isinstance(v, (ProtoBase, RepeatedSequence)):
                    if v._pbf_parent_callback:
                        assert (v._pbf_parent_callback == self._mod_contents), "subobjects can only have one parent--use copy()?"
                    else:
                        v._pbf_parent_callback = self._mod_contents
                        v._pbf_establish_parent_callback = self._establish_parentage_contents
        
            def _set_contents(self, v, modifying=True):
                self._evermod = modifying or self._evermod
                if self._pbf_parent_callback:
                    self._pbf_parent_callback()
                if isinstance(v, (ProtoBase, RepeatedSequence)):
                    self._establish_parentage_contents(v)
                elif isinstance(v, list):
                    list_assign_error = "Can't assign list to repeated field contents"
                    raise ProtoValueError(list_assign_error)
                self._cache[1] = v
                self._mods[1] = ProtoBase.TYPE_string
        
            def _mod_contents(self):
                self._evermod = True
                if self._pbf_parent_callback:
                    self._pbf_parent_callback()
                self._mods[1] = ProtoBase.TYPE_string
        
            def _del_contents(self):
                self._evermod = True
                if self._pbf_parent_callback:
                    self._pbf_parent_callback()
                if 1 in self._cache:
                    del self._cache[1]
                if 1 in self._mods:
                    del self._mods[1]
                self._buf_del(1)
        
            _pb_field_name_1 = "contents"
        
            contents = property(_get_contents, _set_contents, _del_contents)
        
            @property
            def contents__exists(self):
                return 1 in self._mods or self._buf_exists(1)
        
            @property
            def contents__type(self):
                return ProtoBase.TYPE_string
        
            def _finalize_contents(cls):
                if is_string(ProtoBase.TYPE_string):
                    cls._pbf_strings.append(1)
                elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
                    assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
                    if is_string(ProtoBase.TYPE_string.pb_subtype):
                        cls._pbf_strings.append(1)
        
            _pbf_finalizers.append(_finalize_contents)
        
                
            def _get_unknown13(self):
                if 2 in self._cache:
                    r = self._cache[2]
                else:
                    r = self._buf_get(2, ProtoBase.TYPE_int32, 'unknown13')
                    self._cache[2] = r
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
                self._cache[2] = v
                self._mods[2] = ProtoBase.TYPE_int32
        
            def _mod_unknown13(self):
                self._evermod = True
                if self._pbf_parent_callback:
                    self._pbf_parent_callback()
                self._mods[2] = ProtoBase.TYPE_int32
        
            def _del_unknown13(self):
                self._evermod = True
                if self._pbf_parent_callback:
                    self._pbf_parent_callback()
                if 2 in self._cache:
                    del self._cache[2]
                if 2 in self._mods:
                    del self._mods[2]
                self._buf_del(2)
        
            _pb_field_name_2 = "unknown13"
        
            unknown13 = property(_get_unknown13, _set_unknown13, _del_unknown13)
        
            @property
            def unknown13__exists(self):
                return 2 in self._mods or self._buf_exists(2)
        
            @property
            def unknown13__type(self):
                return ProtoBase.TYPE_int32
        
            def _finalize_unknown13(cls):
                if is_string(ProtoBase.TYPE_int32):
                    cls._pbf_strings.append(2)
                elif _PB_type(ProtoBase.TYPE_int32) is _PB_type:
                    assert issubclass(ProtoBase.TYPE_int32, RepeatedSequence)
                    if is_string(ProtoBase.TYPE_int32.pb_subtype):
                        cls._pbf_strings.append(2)
        
            _pbf_finalizers.append(_finalize_unknown13)
        
                
        TYPE_JWT = JWT
        _PB_finalizers.append('Request.AuthInfo.JWT')
            
        TYPE_JWT = JWT
        
        def _get_provider(self):
            if 1 in self._cache:
                r = self._cache[1]
            else:
                r = self._buf_get(1, ProtoBase.TYPE_string, 'provider')
                self._cache[1] = r
            return r
    
        def _establish_parentage_provider(self, v):
            if isinstance(v, (ProtoBase, RepeatedSequence)):
                if v._pbf_parent_callback:
                    assert (v._pbf_parent_callback == self._mod_provider), "subobjects can only have one parent--use copy()?"
                else:
                    v._pbf_parent_callback = self._mod_provider
                    v._pbf_establish_parent_callback = self._establish_parentage_provider
    
        def _set_provider(self, v, modifying=True):
            self._evermod = modifying or self._evermod
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            if isinstance(v, (ProtoBase, RepeatedSequence)):
                self._establish_parentage_provider(v)
            elif isinstance(v, list):
                list_assign_error = "Can't assign list to repeated field provider"
                raise ProtoValueError(list_assign_error)
            self._cache[1] = v
            self._mods[1] = ProtoBase.TYPE_string
    
        def _mod_provider(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            self._mods[1] = ProtoBase.TYPE_string
    
        def _del_provider(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            if 1 in self._cache:
                del self._cache[1]
            if 1 in self._mods:
                del self._mods[1]
            self._buf_del(1)
    
        _pb_field_name_1 = "provider"
    
        provider = property(_get_provider, _set_provider, _del_provider)
    
        @property
        def provider__exists(self):
            return 1 in self._mods or self._buf_exists(1)
    
        @property
        def provider__type(self):
            return ProtoBase.TYPE_string
    
        def _finalize_provider(cls):
            if is_string(ProtoBase.TYPE_string):
                cls._pbf_strings.append(1)
            elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
                assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
                if is_string(ProtoBase.TYPE_string.pb_subtype):
                    cls._pbf_strings.append(1)
    
        _pbf_finalizers.append(_finalize_provider)
    
        
        def _get_token(self):
            if 2 in self._cache:
                r = self._cache[2]
            else:
                r = self._buf_get(2, Request.AuthInfo.TYPE_JWT, 'token')
                self._cache[2] = r
            return r
    
        def _establish_parentage_token(self, v):
            if isinstance(v, (ProtoBase, RepeatedSequence)):
                if v._pbf_parent_callback:
                    assert (v._pbf_parent_callback == self._mod_token), "subobjects can only have one parent--use copy()?"
                else:
                    v._pbf_parent_callback = self._mod_token
                    v._pbf_establish_parent_callback = self._establish_parentage_token
    
        def _set_token(self, v, modifying=True):
            self._evermod = modifying or self._evermod
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            if isinstance(v, (ProtoBase, RepeatedSequence)):
                self._establish_parentage_token(v)
            elif isinstance(v, list):
                list_assign_error = "Can't assign list to repeated field token"
                raise ProtoValueError(list_assign_error)
            self._cache[2] = v
            self._mods[2] = Request.AuthInfo.TYPE_JWT
    
        def _mod_token(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            self._mods[2] = Request.AuthInfo.TYPE_JWT
    
        def _del_token(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            if 2 in self._cache:
                del self._cache[2]
            if 2 in self._mods:
                del self._mods[2]
            self._buf_del(2)
    
        _pb_field_name_2 = "token"
    
        token = property(_get_token, _set_token, _del_token)
    
        @property
        def token__exists(self):
            return 2 in self._mods or self._buf_exists(2)
    
        @property
        def token__type(self):
            return Request.AuthInfo.TYPE_JWT
    
        def _finalize_token(cls):
            if is_string(Request.AuthInfo.TYPE_JWT):
                cls._pbf_strings.append(2)
            elif _PB_type(Request.AuthInfo.TYPE_JWT) is _PB_type:
                assert issubclass(Request.AuthInfo.TYPE_JWT, RepeatedSequence)
                if is_string(Request.AuthInfo.TYPE_JWT.pb_subtype):
                    cls._pbf_strings.append(2)
    
        _pbf_finalizers.append(_finalize_token)
    
        
    TYPE_AuthInfo = AuthInfo
    _PB_finalizers.append('Request.AuthInfo')
    
    TYPE_AuthInfo = AuthInfo
    
    class Unknown3(ProtoBase):
        _required = [1]
        _field_map = {'unknown4': 1}
        
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
            return ['unknown4']
    
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
        
        def _get_unknown4(self):
            if 1 in self._cache:
                r = self._cache[1]
            else:
                r = self._buf_get(1, ProtoBase.TYPE_string, 'unknown4')
                self._cache[1] = r
            return r
    
        def _establish_parentage_unknown4(self, v):
            if isinstance(v, (ProtoBase, RepeatedSequence)):
                if v._pbf_parent_callback:
                    assert (v._pbf_parent_callback == self._mod_unknown4), "subobjects can only have one parent--use copy()?"
                else:
                    v._pbf_parent_callback = self._mod_unknown4
                    v._pbf_establish_parent_callback = self._establish_parentage_unknown4
    
        def _set_unknown4(self, v, modifying=True):
            self._evermod = modifying or self._evermod
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            if isinstance(v, (ProtoBase, RepeatedSequence)):
                self._establish_parentage_unknown4(v)
            elif isinstance(v, list):
                list_assign_error = "Can't assign list to repeated field unknown4"
                raise ProtoValueError(list_assign_error)
            self._cache[1] = v
            self._mods[1] = ProtoBase.TYPE_string
    
        def _mod_unknown4(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            self._mods[1] = ProtoBase.TYPE_string
    
        def _del_unknown4(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            if 1 in self._cache:
                del self._cache[1]
            if 1 in self._mods:
                del self._mods[1]
            self._buf_del(1)
    
        _pb_field_name_1 = "unknown4"
    
        unknown4 = property(_get_unknown4, _set_unknown4, _del_unknown4)
    
        @property
        def unknown4__exists(self):
            return 1 in self._mods or self._buf_exists(1)
    
        @property
        def unknown4__type(self):
            return ProtoBase.TYPE_string
    
        def _finalize_unknown4(cls):
            if is_string(ProtoBase.TYPE_string):
                cls._pbf_strings.append(1)
            elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
                assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
                if is_string(ProtoBase.TYPE_string.pb_subtype):
                    cls._pbf_strings.append(1)
    
        _pbf_finalizers.append(_finalize_unknown4)
    
        
    TYPE_Unknown3 = Unknown3
    _PB_finalizers.append('Request.Unknown3')
    
    TYPE_Unknown3 = Unknown3
    
    class Unknown6(ProtoBase):
        _required = [1, 2]
        _field_map = {'unknown2': 2, 'unknown1': 1}
        
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
            return ['unknown1', 'unknown2']
    
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
            
        class Unknown2(ProtoBase):
            _required = [1]
            _field_map = {'unknown1': 1}
            
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
                return ['unknown1']
        
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
                    r = self._buf_get(1, ProtoBase.TYPE_bytes, 'unknown1')
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
                self._mods[1] = ProtoBase.TYPE_bytes
        
            def _mod_unknown1(self):
                self._evermod = True
                if self._pbf_parent_callback:
                    self._pbf_parent_callback()
                self._mods[1] = ProtoBase.TYPE_bytes
        
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
                return ProtoBase.TYPE_bytes
        
            def _finalize_unknown1(cls):
                if is_string(ProtoBase.TYPE_bytes):
                    cls._pbf_strings.append(1)
                elif _PB_type(ProtoBase.TYPE_bytes) is _PB_type:
                    assert issubclass(ProtoBase.TYPE_bytes, RepeatedSequence)
                    if is_string(ProtoBase.TYPE_bytes.pb_subtype):
                        cls._pbf_strings.append(1)
        
            _pbf_finalizers.append(_finalize_unknown1)
        
                
        TYPE_Unknown2 = Unknown2
        _PB_finalizers.append('Request.Unknown6.Unknown2')
            
        TYPE_Unknown2 = Unknown2
        
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
    
        
        def _get_unknown2(self):
            if 2 in self._cache:
                r = self._cache[2]
            else:
                r = self._buf_get(2, Request.Unknown6.TYPE_Unknown2, 'unknown2')
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
            self._mods[2] = Request.Unknown6.TYPE_Unknown2
    
        def _mod_unknown2(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            self._mods[2] = Request.Unknown6.TYPE_Unknown2
    
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
            return Request.Unknown6.TYPE_Unknown2
    
        def _finalize_unknown2(cls):
            if is_string(Request.Unknown6.TYPE_Unknown2):
                cls._pbf_strings.append(2)
            elif _PB_type(Request.Unknown6.TYPE_Unknown2) is _PB_type:
                assert issubclass(Request.Unknown6.TYPE_Unknown2, RepeatedSequence)
                if is_string(Request.Unknown6.TYPE_Unknown2.pb_subtype):
                    cls._pbf_strings.append(2)
    
        _pbf_finalizers.append(_finalize_unknown2)
    
        
    TYPE_Unknown6 = Unknown6
    _PB_finalizers.append('Request.Unknown6')
    
    TYPE_Unknown6 = Unknown6

    def _get_direction(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, RpcEnum_palm.TYPE_RpcDirection, 'direction')
            self._cache[1] = r
        return r

    def _establish_parentage_direction(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_direction), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_direction
                v._pbf_establish_parent_callback = self._establish_parentage_direction

    def _set_direction(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_direction(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field direction"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = RpcEnum_palm.TYPE_RpcDirection

    def _mod_direction(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = RpcEnum_palm.TYPE_RpcDirection

    def _del_direction(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "direction"

    direction = property(_get_direction, _set_direction, _del_direction)

    @property
    def direction__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def direction__type(self):
        return RpcEnum_palm.TYPE_RpcDirection

    def _finalize_direction(cls):
        if is_string(RpcEnum_palm.TYPE_RpcDirection):
            cls._pbf_strings.append(1)
        elif _PB_type(RpcEnum_palm.TYPE_RpcDirection) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_RpcDirection, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_RpcDirection.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_direction)


    def _get_rpc_id(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_int64, 'rpc_id')
            self._cache[3] = r
        return r

    def _establish_parentage_rpc_id(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_rpc_id), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_rpc_id
                v._pbf_establish_parent_callback = self._establish_parentage_rpc_id

    def _set_rpc_id(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_rpc_id(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field rpc_id"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_int64

    def _mod_rpc_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_int64

    def _del_rpc_id(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "rpc_id"

    rpc_id = property(_get_rpc_id, _set_rpc_id, _del_rpc_id)

    @property
    def rpc_id__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def rpc_id__type(self):
        return ProtoBase.TYPE_int64

    def _finalize_rpc_id(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_rpc_id)


    class Repeated_requests(RepeatedSequence):
        class pb_subtype(object):
            def __get__(self, instance, cls):
                return Request.TYPE_Requests
        pb_subtype = pb_subtype()


    TYPE_Repeated_requests = Repeated_requests


    @property
    def requests__stream(self):
        if 4 in self._cache:
            def acc(v):
                v_ = lambda: v
                return v_
            return [acc(v) for v in self._cache[4]]
        return self._get_repeated(4, self.TYPE_Repeated_requests, "requests", lazy=True)

    def requests__fast_append(self, value):
        self._append_to_repeated(4, self.TYPE_Repeated_requests, value)

    def _get_requests(self):
        if 4 in self._cache:
            r = self._cache[4]
        else:
            r = self._buf_get(4, self.TYPE_Repeated_requests, 'requests')
            self._cache[4] = r
        return r

    def _establish_parentage_requests(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_requests), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_requests
                v._pbf_establish_parent_callback = self._establish_parentage_requests

    def _set_requests(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_requests(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field requests"
            raise ProtoValueError(list_assign_error)
        self._cache[4] = v
        self._mods[4] = self.TYPE_Repeated_requests

    def _mod_requests(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[4] = self.TYPE_Repeated_requests

    def _del_requests(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 4 in self._cache:
            del self._cache[4]
        if 4 in self._mods:
            del self._mods[4]
        self._buf_del(4)

    _pb_field_name_4 = "requests"

    requests = property(_get_requests, _set_requests, _del_requests)

    @property
    def requests__exists(self):
        return 4 in self._mods or self._buf_exists(4)

    @property
    def requests__type(self):
        return self.TYPE_Repeated_requests

    def _finalize_requests(cls):
        if is_string(cls.TYPE_Repeated_requests):
            cls._pbf_strings.append(4)
        elif _PB_type(cls.TYPE_Repeated_requests) is _PB_type:
            assert issubclass(cls.TYPE_Repeated_requests, RepeatedSequence)
            if is_string(cls.TYPE_Repeated_requests.pb_subtype):
                cls._pbf_strings.append(4)

    _pbf_finalizers.append(_finalize_requests)


    def _get_unknown6(self):
        if 6 in self._cache:
            r = self._cache[6]
        else:
            r = self._buf_get(6, Request.TYPE_Unknown6, 'unknown6')
            self._cache[6] = r
        return r

    def _establish_parentage_unknown6(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_unknown6), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_unknown6
                v._pbf_establish_parent_callback = self._establish_parentage_unknown6

    def _set_unknown6(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_unknown6(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field unknown6"
            raise ProtoValueError(list_assign_error)
        self._cache[6] = v
        self._mods[6] = Request.TYPE_Unknown6

    def _mod_unknown6(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[6] = Request.TYPE_Unknown6

    def _del_unknown6(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 6 in self._cache:
            del self._cache[6]
        if 6 in self._mods:
            del self._mods[6]
        self._buf_del(6)

    _pb_field_name_6 = "unknown6"

    unknown6 = property(_get_unknown6, _set_unknown6, _del_unknown6)

    @property
    def unknown6__exists(self):
        return 6 in self._mods or self._buf_exists(6)

    @property
    def unknown6__type(self):
        return Request.TYPE_Unknown6

    def _finalize_unknown6(cls):
        if is_string(Request.TYPE_Unknown6):
            cls._pbf_strings.append(6)
        elif _PB_type(Request.TYPE_Unknown6) is _PB_type:
            assert issubclass(Request.TYPE_Unknown6, RepeatedSequence)
            if is_string(Request.TYPE_Unknown6.pb_subtype):
                cls._pbf_strings.append(6)

    _pbf_finalizers.append(_finalize_unknown6)


    def _get_latitude(self):
        if 7 in self._cache:
            r = self._cache[7]
        else:
            r = self._buf_get(7, ProtoBase.TYPE_fixed64, 'latitude')
            self._cache[7] = r
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
        self._cache[7] = v
        self._mods[7] = ProtoBase.TYPE_fixed64

    def _mod_latitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[7] = ProtoBase.TYPE_fixed64

    def _del_latitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 7 in self._cache:
            del self._cache[7]
        if 7 in self._mods:
            del self._mods[7]
        self._buf_del(7)

    _pb_field_name_7 = "latitude"

    latitude = property(_get_latitude, _set_latitude, _del_latitude)

    @property
    def latitude__exists(self):
        return 7 in self._mods or self._buf_exists(7)

    @property
    def latitude__type(self):
        return ProtoBase.TYPE_fixed64

    def _finalize_latitude(cls):
        if is_string(ProtoBase.TYPE_fixed64):
            cls._pbf_strings.append(7)
        elif _PB_type(ProtoBase.TYPE_fixed64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_fixed64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_fixed64.pb_subtype):
                cls._pbf_strings.append(7)

    _pbf_finalizers.append(_finalize_latitude)


    def _get_longitude(self):
        if 8 in self._cache:
            r = self._cache[8]
        else:
            r = self._buf_get(8, ProtoBase.TYPE_fixed64, 'longitude')
            self._cache[8] = r
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
        self._cache[8] = v
        self._mods[8] = ProtoBase.TYPE_fixed64

    def _mod_longitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[8] = ProtoBase.TYPE_fixed64

    def _del_longitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 8 in self._cache:
            del self._cache[8]
        if 8 in self._mods:
            del self._mods[8]
        self._buf_del(8)

    _pb_field_name_8 = "longitude"

    longitude = property(_get_longitude, _set_longitude, _del_longitude)

    @property
    def longitude__exists(self):
        return 8 in self._mods or self._buf_exists(8)

    @property
    def longitude__type(self):
        return ProtoBase.TYPE_fixed64

    def _finalize_longitude(cls):
        if is_string(ProtoBase.TYPE_fixed64):
            cls._pbf_strings.append(8)
        elif _PB_type(ProtoBase.TYPE_fixed64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_fixed64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_fixed64.pb_subtype):
                cls._pbf_strings.append(8)

    _pbf_finalizers.append(_finalize_longitude)


    def _get_altitude(self):
        if 9 in self._cache:
            r = self._cache[9]
        else:
            r = self._buf_get(9, ProtoBase.TYPE_fixed64, 'altitude')
            self._cache[9] = r
        return r

    def _establish_parentage_altitude(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_altitude), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_altitude
                v._pbf_establish_parent_callback = self._establish_parentage_altitude

    def _set_altitude(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_altitude(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field altitude"
            raise ProtoValueError(list_assign_error)
        self._cache[9] = v
        self._mods[9] = ProtoBase.TYPE_fixed64

    def _mod_altitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[9] = ProtoBase.TYPE_fixed64

    def _del_altitude(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 9 in self._cache:
            del self._cache[9]
        if 9 in self._mods:
            del self._mods[9]
        self._buf_del(9)

    _pb_field_name_9 = "altitude"

    altitude = property(_get_altitude, _set_altitude, _del_altitude)

    @property
    def altitude__exists(self):
        return 9 in self._mods or self._buf_exists(9)

    @property
    def altitude__type(self):
        return ProtoBase.TYPE_fixed64

    def _finalize_altitude(cls):
        if is_string(ProtoBase.TYPE_fixed64):
            cls._pbf_strings.append(9)
        elif _PB_type(ProtoBase.TYPE_fixed64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_fixed64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_fixed64.pb_subtype):
                cls._pbf_strings.append(9)

    _pbf_finalizers.append(_finalize_altitude)


    def _get_auth(self):
        if 10 in self._cache:
            r = self._cache[10]
        else:
            r = self._buf_get(10, Request.TYPE_AuthInfo, 'auth')
            self._cache[10] = r
        return r

    def _establish_parentage_auth(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_auth), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_auth
                v._pbf_establish_parent_callback = self._establish_parentage_auth

    def _set_auth(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_auth(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field auth"
            raise ProtoValueError(list_assign_error)
        self._cache[10] = v
        self._mods[10] = Request.TYPE_AuthInfo

    def _mod_auth(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[10] = Request.TYPE_AuthInfo

    def _del_auth(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 10 in self._cache:
            del self._cache[10]
        if 10 in self._mods:
            del self._mods[10]
        self._buf_del(10)

    _pb_field_name_10 = "auth"

    auth = property(_get_auth, _set_auth, _del_auth)

    @property
    def auth__exists(self):
        return 10 in self._mods or self._buf_exists(10)

    @property
    def auth__type(self):
        return Request.TYPE_AuthInfo

    def _finalize_auth(cls):
        if is_string(Request.TYPE_AuthInfo):
            cls._pbf_strings.append(10)
        elif _PB_type(Request.TYPE_AuthInfo) is _PB_type:
            assert issubclass(Request.TYPE_AuthInfo, RepeatedSequence)
            if is_string(Request.TYPE_AuthInfo.pb_subtype):
                cls._pbf_strings.append(10)

    _pbf_finalizers.append(_finalize_auth)


    def _get_auth_ticket(self):
        if 11 in self._cache:
            r = self._cache[11]
        else:
            r = self._buf_get(11, TYPE_AuthTicket, 'auth_ticket')
            self._cache[11] = r
        return r

    def _establish_parentage_auth_ticket(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_auth_ticket), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_auth_ticket
                v._pbf_establish_parent_callback = self._establish_parentage_auth_ticket

    def _set_auth_ticket(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_auth_ticket(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field auth_ticket"
            raise ProtoValueError(list_assign_error)
        self._cache[11] = v
        self._mods[11] = TYPE_AuthTicket

    def _mod_auth_ticket(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[11] = TYPE_AuthTicket

    def _del_auth_ticket(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 11 in self._cache:
            del self._cache[11]
        if 11 in self._mods:
            del self._mods[11]
        self._buf_del(11)

    _pb_field_name_11 = "auth_ticket"

    auth_ticket = property(_get_auth_ticket, _set_auth_ticket, _del_auth_ticket)

    @property
    def auth_ticket__exists(self):
        return 11 in self._mods or self._buf_exists(11)

    @property
    def auth_ticket__type(self):
        return TYPE_AuthTicket

    def _finalize_auth_ticket(cls):
        if is_string(TYPE_AuthTicket):
            cls._pbf_strings.append(11)
        elif _PB_type(TYPE_AuthTicket) is _PB_type:
            assert issubclass(TYPE_AuthTicket, RepeatedSequence)
            if is_string(TYPE_AuthTicket.pb_subtype):
                cls._pbf_strings.append(11)

    _pbf_finalizers.append(_finalize_auth_ticket)


    def _get_unknown12(self):
        if 12 in self._cache:
            r = self._cache[12]
        else:
            r = self._buf_get(12, ProtoBase.TYPE_int64, 'unknown12')
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
        self._mods[12] = ProtoBase.TYPE_int64

    def _mod_unknown12(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[12] = ProtoBase.TYPE_int64

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
        return ProtoBase.TYPE_int64

    def _finalize_unknown12(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(12)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(12)

    _pbf_finalizers.append(_finalize_unknown12)


TYPE_Request = Request
_PB_finalizers.append('Request')

class Response(ProtoBase):
    _required = [1, 6]
    _field_map = {'direction': 1, 'api_url': 3, 'auth_ticket': 7, 'unknown2': 2, 'unknown6': 6, 'responses': 100}
    
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
        return ['direction', 'unknown2', 'api_url', 'responses', 'unknown6', 'auth_ticket']

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
    
    class Unknown6(ProtoBase):
        _required = [1, 2]
        _field_map = {'unknown2': 2, 'unknown1': 1}
        
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
            return ['unknown1', 'unknown2']
    
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
            
        class Unknown2(ProtoBase):
            _required = [1]
            _field_map = {'unknown1': 1}
            
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
                return ['unknown1']
        
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
                    r = self._buf_get(1, ProtoBase.TYPE_bytes, 'unknown1')
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
                self._mods[1] = ProtoBase.TYPE_bytes
        
            def _mod_unknown1(self):
                self._evermod = True
                if self._pbf_parent_callback:
                    self._pbf_parent_callback()
                self._mods[1] = ProtoBase.TYPE_bytes
        
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
                return ProtoBase.TYPE_bytes
        
            def _finalize_unknown1(cls):
                if is_string(ProtoBase.TYPE_bytes):
                    cls._pbf_strings.append(1)
                elif _PB_type(ProtoBase.TYPE_bytes) is _PB_type:
                    assert issubclass(ProtoBase.TYPE_bytes, RepeatedSequence)
                    if is_string(ProtoBase.TYPE_bytes.pb_subtype):
                        cls._pbf_strings.append(1)
        
            _pbf_finalizers.append(_finalize_unknown1)
        
                
        TYPE_Unknown2 = Unknown2
        _PB_finalizers.append('Response.Unknown6.Unknown2')
            
        TYPE_Unknown2 = Unknown2
        
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
    
        
        def _get_unknown2(self):
            if 2 in self._cache:
                r = self._cache[2]
            else:
                r = self._buf_get(2, Response.Unknown6.TYPE_Unknown2, 'unknown2')
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
            self._mods[2] = Response.Unknown6.TYPE_Unknown2
    
        def _mod_unknown2(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            self._mods[2] = Response.Unknown6.TYPE_Unknown2
    
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
            return Response.Unknown6.TYPE_Unknown2
    
        def _finalize_unknown2(cls):
            if is_string(Response.Unknown6.TYPE_Unknown2):
                cls._pbf_strings.append(2)
            elif _PB_type(Response.Unknown6.TYPE_Unknown2) is _PB_type:
                assert issubclass(Response.Unknown6.TYPE_Unknown2, RepeatedSequence)
                if is_string(Response.Unknown6.TYPE_Unknown2.pb_subtype):
                    cls._pbf_strings.append(2)
    
        _pbf_finalizers.append(_finalize_unknown2)
    
        
    TYPE_Unknown6 = Unknown6
    _PB_finalizers.append('Response.Unknown6')
    
    TYPE_Unknown6 = Unknown6
    
    class Unknown7(ProtoBase):
        _required = []
        _field_map = {'unknown72': 2, 'unknown73': 3, 'unknown71': 1}
        
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
            return ['unknown71', 'unknown72', 'unknown73']
    
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
        
        def _get_unknown71(self):
            if 1 in self._cache:
                r = self._cache[1]
            else:
                r = self._buf_get(1, ProtoBase.TYPE_bytes, 'unknown71')
                self._cache[1] = r
            return r
    
        def _establish_parentage_unknown71(self, v):
            if isinstance(v, (ProtoBase, RepeatedSequence)):
                if v._pbf_parent_callback:
                    assert (v._pbf_parent_callback == self._mod_unknown71), "subobjects can only have one parent--use copy()?"
                else:
                    v._pbf_parent_callback = self._mod_unknown71
                    v._pbf_establish_parent_callback = self._establish_parentage_unknown71
    
        def _set_unknown71(self, v, modifying=True):
            self._evermod = modifying or self._evermod
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            if isinstance(v, (ProtoBase, RepeatedSequence)):
                self._establish_parentage_unknown71(v)
            elif isinstance(v, list):
                list_assign_error = "Can't assign list to repeated field unknown71"
                raise ProtoValueError(list_assign_error)
            self._cache[1] = v
            self._mods[1] = ProtoBase.TYPE_bytes
    
        def _mod_unknown71(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            self._mods[1] = ProtoBase.TYPE_bytes
    
        def _del_unknown71(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            if 1 in self._cache:
                del self._cache[1]
            if 1 in self._mods:
                del self._mods[1]
            self._buf_del(1)
    
        _pb_field_name_1 = "unknown71"
    
        unknown71 = property(_get_unknown71, _set_unknown71, _del_unknown71)
    
        @property
        def unknown71__exists(self):
            return 1 in self._mods or self._buf_exists(1)
    
        @property
        def unknown71__type(self):
            return ProtoBase.TYPE_bytes
    
        def _finalize_unknown71(cls):
            if is_string(ProtoBase.TYPE_bytes):
                cls._pbf_strings.append(1)
            elif _PB_type(ProtoBase.TYPE_bytes) is _PB_type:
                assert issubclass(ProtoBase.TYPE_bytes, RepeatedSequence)
                if is_string(ProtoBase.TYPE_bytes.pb_subtype):
                    cls._pbf_strings.append(1)
    
        _pbf_finalizers.append(_finalize_unknown71)
    
        
        def _get_unknown72(self):
            if 2 in self._cache:
                r = self._cache[2]
            else:
                r = self._buf_get(2, ProtoBase.TYPE_int64, 'unknown72')
                self._cache[2] = r
            return r
    
        def _establish_parentage_unknown72(self, v):
            if isinstance(v, (ProtoBase, RepeatedSequence)):
                if v._pbf_parent_callback:
                    assert (v._pbf_parent_callback == self._mod_unknown72), "subobjects can only have one parent--use copy()?"
                else:
                    v._pbf_parent_callback = self._mod_unknown72
                    v._pbf_establish_parent_callback = self._establish_parentage_unknown72
    
        def _set_unknown72(self, v, modifying=True):
            self._evermod = modifying or self._evermod
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            if isinstance(v, (ProtoBase, RepeatedSequence)):
                self._establish_parentage_unknown72(v)
            elif isinstance(v, list):
                list_assign_error = "Can't assign list to repeated field unknown72"
                raise ProtoValueError(list_assign_error)
            self._cache[2] = v
            self._mods[2] = ProtoBase.TYPE_int64
    
        def _mod_unknown72(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            self._mods[2] = ProtoBase.TYPE_int64
    
        def _del_unknown72(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            if 2 in self._cache:
                del self._cache[2]
            if 2 in self._mods:
                del self._mods[2]
            self._buf_del(2)
    
        _pb_field_name_2 = "unknown72"
    
        unknown72 = property(_get_unknown72, _set_unknown72, _del_unknown72)
    
        @property
        def unknown72__exists(self):
            return 2 in self._mods or self._buf_exists(2)
    
        @property
        def unknown72__type(self):
            return ProtoBase.TYPE_int64
    
        def _finalize_unknown72(cls):
            if is_string(ProtoBase.TYPE_int64):
                cls._pbf_strings.append(2)
            elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
                assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
                if is_string(ProtoBase.TYPE_int64.pb_subtype):
                    cls._pbf_strings.append(2)
    
        _pbf_finalizers.append(_finalize_unknown72)
    
        
        def _get_unknown73(self):
            if 3 in self._cache:
                r = self._cache[3]
            else:
                r = self._buf_get(3, ProtoBase.TYPE_bytes, 'unknown73')
                self._cache[3] = r
            return r
    
        def _establish_parentage_unknown73(self, v):
            if isinstance(v, (ProtoBase, RepeatedSequence)):
                if v._pbf_parent_callback:
                    assert (v._pbf_parent_callback == self._mod_unknown73), "subobjects can only have one parent--use copy()?"
                else:
                    v._pbf_parent_callback = self._mod_unknown73
                    v._pbf_establish_parent_callback = self._establish_parentage_unknown73
    
        def _set_unknown73(self, v, modifying=True):
            self._evermod = modifying or self._evermod
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            if isinstance(v, (ProtoBase, RepeatedSequence)):
                self._establish_parentage_unknown73(v)
            elif isinstance(v, list):
                list_assign_error = "Can't assign list to repeated field unknown73"
                raise ProtoValueError(list_assign_error)
            self._cache[3] = v
            self._mods[3] = ProtoBase.TYPE_bytes
    
        def _mod_unknown73(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            self._mods[3] = ProtoBase.TYPE_bytes
    
        def _del_unknown73(self):
            self._evermod = True
            if self._pbf_parent_callback:
                self._pbf_parent_callback()
            if 3 in self._cache:
                del self._cache[3]
            if 3 in self._mods:
                del self._mods[3]
            self._buf_del(3)
    
        _pb_field_name_3 = "unknown73"
    
        unknown73 = property(_get_unknown73, _set_unknown73, _del_unknown73)
    
        @property
        def unknown73__exists(self):
            return 3 in self._mods or self._buf_exists(3)
    
        @property
        def unknown73__type(self):
            return ProtoBase.TYPE_bytes
    
        def _finalize_unknown73(cls):
            if is_string(ProtoBase.TYPE_bytes):
                cls._pbf_strings.append(3)
            elif _PB_type(ProtoBase.TYPE_bytes) is _PB_type:
                assert issubclass(ProtoBase.TYPE_bytes, RepeatedSequence)
                if is_string(ProtoBase.TYPE_bytes.pb_subtype):
                    cls._pbf_strings.append(3)
    
        _pbf_finalizers.append(_finalize_unknown73)
    
        
    TYPE_Unknown7 = Unknown7
    _PB_finalizers.append('Response.Unknown7')
    
    TYPE_Unknown7 = Unknown7

    def _get_direction(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, RpcEnum_palm.TYPE_RpcDirection, 'direction')
            self._cache[1] = r
        return r

    def _establish_parentage_direction(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_direction), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_direction
                v._pbf_establish_parent_callback = self._establish_parentage_direction

    def _set_direction(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_direction(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field direction"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = RpcEnum_palm.TYPE_RpcDirection

    def _mod_direction(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = RpcEnum_palm.TYPE_RpcDirection

    def _del_direction(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "direction"

    direction = property(_get_direction, _set_direction, _del_direction)

    @property
    def direction__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def direction__type(self):
        return RpcEnum_palm.TYPE_RpcDirection

    def _finalize_direction(cls):
        if is_string(RpcEnum_palm.TYPE_RpcDirection):
            cls._pbf_strings.append(1)
        elif _PB_type(RpcEnum_palm.TYPE_RpcDirection) is _PB_type:
            assert issubclass(RpcEnum_palm.TYPE_RpcDirection, RepeatedSequence)
            if is_string(RpcEnum_palm.TYPE_RpcDirection.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_direction)


    def _get_unknown2(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_int64, 'unknown2')
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
        self._mods[2] = ProtoBase.TYPE_int64

    def _mod_unknown2(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_int64

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
        return ProtoBase.TYPE_int64

    def _finalize_unknown2(cls):
        if is_string(ProtoBase.TYPE_int64):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_int64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_int64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_int64.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_unknown2)


    def _get_api_url(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_string, 'api_url')
            self._cache[3] = r
        return r

    def _establish_parentage_api_url(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_api_url), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_api_url
                v._pbf_establish_parent_callback = self._establish_parentage_api_url

    def _set_api_url(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_api_url(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field api_url"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_string

    def _mod_api_url(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_string

    def _del_api_url(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "api_url"

    api_url = property(_get_api_url, _set_api_url, _del_api_url)

    @property
    def api_url__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def api_url__type(self):
        return ProtoBase.TYPE_string

    def _finalize_api_url(cls):
        if is_string(ProtoBase.TYPE_string):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_string) is _PB_type:
            assert issubclass(ProtoBase.TYPE_string, RepeatedSequence)
            if is_string(ProtoBase.TYPE_string.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_api_url)


    class Repeated_responses(RepeatedSequence):
        class pb_subtype(object):
            def __get__(self, instance, cls):
                return ProtoBase.TYPE_bytes
        pb_subtype = pb_subtype()


    TYPE_Repeated_responses = Repeated_responses


    def _get_responses(self):
        if 100 in self._cache:
            r = self._cache[100]
        else:
            r = self._buf_get(100, self.TYPE_Repeated_responses, 'responses')
            self._cache[100] = r
        return r

    def _establish_parentage_responses(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_responses), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_responses
                v._pbf_establish_parent_callback = self._establish_parentage_responses

    def _set_responses(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_responses(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field responses"
            raise ProtoValueError(list_assign_error)
        self._cache[100] = v
        self._mods[100] = self.TYPE_Repeated_responses

    def _mod_responses(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[100] = self.TYPE_Repeated_responses

    def _del_responses(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 100 in self._cache:
            del self._cache[100]
        if 100 in self._mods:
            del self._mods[100]
        self._buf_del(100)

    _pb_field_name_100 = "responses"

    responses = property(_get_responses, _set_responses, _del_responses)

    @property
    def responses__exists(self):
        return 100 in self._mods or self._buf_exists(100)

    @property
    def responses__type(self):
        return self.TYPE_Repeated_responses

    def _finalize_responses(cls):
        if is_string(cls.TYPE_Repeated_responses):
            cls._pbf_strings.append(100)
        elif _PB_type(cls.TYPE_Repeated_responses) is _PB_type:
            assert issubclass(cls.TYPE_Repeated_responses, RepeatedSequence)
            if is_string(cls.TYPE_Repeated_responses.pb_subtype):
                cls._pbf_strings.append(100)

    _pbf_finalizers.append(_finalize_responses)


    def _get_unknown6(self):
        if 6 in self._cache:
            r = self._cache[6]
        else:
            r = self._buf_get(6, Response.TYPE_Unknown6, 'unknown6')
            self._cache[6] = r
        return r

    def _establish_parentage_unknown6(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_unknown6), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_unknown6
                v._pbf_establish_parent_callback = self._establish_parentage_unknown6

    def _set_unknown6(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_unknown6(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field unknown6"
            raise ProtoValueError(list_assign_error)
        self._cache[6] = v
        self._mods[6] = Response.TYPE_Unknown6

    def _mod_unknown6(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[6] = Response.TYPE_Unknown6

    def _del_unknown6(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 6 in self._cache:
            del self._cache[6]
        if 6 in self._mods:
            del self._mods[6]
        self._buf_del(6)

    _pb_field_name_6 = "unknown6"

    unknown6 = property(_get_unknown6, _set_unknown6, _del_unknown6)

    @property
    def unknown6__exists(self):
        return 6 in self._mods or self._buf_exists(6)

    @property
    def unknown6__type(self):
        return Response.TYPE_Unknown6

    def _finalize_unknown6(cls):
        if is_string(Response.TYPE_Unknown6):
            cls._pbf_strings.append(6)
        elif _PB_type(Response.TYPE_Unknown6) is _PB_type:
            assert issubclass(Response.TYPE_Unknown6, RepeatedSequence)
            if is_string(Response.TYPE_Unknown6.pb_subtype):
                cls._pbf_strings.append(6)

    _pbf_finalizers.append(_finalize_unknown6)


    def _get_auth_ticket(self):
        if 7 in self._cache:
            r = self._cache[7]
        else:
            r = self._buf_get(7, TYPE_AuthTicket, 'auth_ticket')
            self._cache[7] = r
        return r

    def _establish_parentage_auth_ticket(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_auth_ticket), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_auth_ticket
                v._pbf_establish_parent_callback = self._establish_parentage_auth_ticket

    def _set_auth_ticket(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_auth_ticket(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field auth_ticket"
            raise ProtoValueError(list_assign_error)
        self._cache[7] = v
        self._mods[7] = TYPE_AuthTicket

    def _mod_auth_ticket(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[7] = TYPE_AuthTicket

    def _del_auth_ticket(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 7 in self._cache:
            del self._cache[7]
        if 7 in self._mods:
            del self._mods[7]
        self._buf_del(7)

    _pb_field_name_7 = "auth_ticket"

    auth_ticket = property(_get_auth_ticket, _set_auth_ticket, _del_auth_ticket)

    @property
    def auth_ticket__exists(self):
        return 7 in self._mods or self._buf_exists(7)

    @property
    def auth_ticket__type(self):
        return TYPE_AuthTicket

    def _finalize_auth_ticket(cls):
        if is_string(TYPE_AuthTicket):
            cls._pbf_strings.append(7)
        elif _PB_type(TYPE_AuthTicket) is _PB_type:
            assert issubclass(TYPE_AuthTicket, RepeatedSequence)
            if is_string(TYPE_AuthTicket.pb_subtype):
                cls._pbf_strings.append(7)

    _pbf_finalizers.append(_finalize_auth_ticket)


TYPE_Response = Response
_PB_finalizers.append('Response')

class AuthTicket(ProtoBase):
    _required = []
    _field_map = {'expire_timestamp_ms': 2, 'start': 1, 'end': 3}
    
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
        return ['start', 'expire_timestamp_ms', 'end']

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

    def _get_start(self):
        if 1 in self._cache:
            r = self._cache[1]
        else:
            r = self._buf_get(1, ProtoBase.TYPE_bytes, 'start')
            self._cache[1] = r
        return r

    def _establish_parentage_start(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_start), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_start
                v._pbf_establish_parent_callback = self._establish_parentage_start

    def _set_start(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_start(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field start"
            raise ProtoValueError(list_assign_error)
        self._cache[1] = v
        self._mods[1] = ProtoBase.TYPE_bytes

    def _mod_start(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[1] = ProtoBase.TYPE_bytes

    def _del_start(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 1 in self._cache:
            del self._cache[1]
        if 1 in self._mods:
            del self._mods[1]
        self._buf_del(1)

    _pb_field_name_1 = "start"

    start = property(_get_start, _set_start, _del_start)

    @property
    def start__exists(self):
        return 1 in self._mods or self._buf_exists(1)

    @property
    def start__type(self):
        return ProtoBase.TYPE_bytes

    def _finalize_start(cls):
        if is_string(ProtoBase.TYPE_bytes):
            cls._pbf_strings.append(1)
        elif _PB_type(ProtoBase.TYPE_bytes) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bytes, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bytes.pb_subtype):
                cls._pbf_strings.append(1)

    _pbf_finalizers.append(_finalize_start)


    def _get_expire_timestamp_ms(self):
        if 2 in self._cache:
            r = self._cache[2]
        else:
            r = self._buf_get(2, ProtoBase.TYPE_uint64, 'expire_timestamp_ms')
            self._cache[2] = r
        return r

    def _establish_parentage_expire_timestamp_ms(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_expire_timestamp_ms), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_expire_timestamp_ms
                v._pbf_establish_parent_callback = self._establish_parentage_expire_timestamp_ms

    def _set_expire_timestamp_ms(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_expire_timestamp_ms(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field expire_timestamp_ms"
            raise ProtoValueError(list_assign_error)
        self._cache[2] = v
        self._mods[2] = ProtoBase.TYPE_uint64

    def _mod_expire_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[2] = ProtoBase.TYPE_uint64

    def _del_expire_timestamp_ms(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 2 in self._cache:
            del self._cache[2]
        if 2 in self._mods:
            del self._mods[2]
        self._buf_del(2)

    _pb_field_name_2 = "expire_timestamp_ms"

    expire_timestamp_ms = property(_get_expire_timestamp_ms, _set_expire_timestamp_ms, _del_expire_timestamp_ms)

    @property
    def expire_timestamp_ms__exists(self):
        return 2 in self._mods or self._buf_exists(2)

    @property
    def expire_timestamp_ms__type(self):
        return ProtoBase.TYPE_uint64

    def _finalize_expire_timestamp_ms(cls):
        if is_string(ProtoBase.TYPE_uint64):
            cls._pbf_strings.append(2)
        elif _PB_type(ProtoBase.TYPE_uint64) is _PB_type:
            assert issubclass(ProtoBase.TYPE_uint64, RepeatedSequence)
            if is_string(ProtoBase.TYPE_uint64.pb_subtype):
                cls._pbf_strings.append(2)

    _pbf_finalizers.append(_finalize_expire_timestamp_ms)


    def _get_end(self):
        if 3 in self._cache:
            r = self._cache[3]
        else:
            r = self._buf_get(3, ProtoBase.TYPE_bytes, 'end')
            self._cache[3] = r
        return r

    def _establish_parentage_end(self, v):
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            if v._pbf_parent_callback:
                assert (v._pbf_parent_callback == self._mod_end), "subobjects can only have one parent--use copy()?"
            else:
                v._pbf_parent_callback = self._mod_end
                v._pbf_establish_parent_callback = self._establish_parentage_end

    def _set_end(self, v, modifying=True):
        self._evermod = modifying or self._evermod
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if isinstance(v, (ProtoBase, RepeatedSequence)):
            self._establish_parentage_end(v)
        elif isinstance(v, list):
            list_assign_error = "Can't assign list to repeated field end"
            raise ProtoValueError(list_assign_error)
        self._cache[3] = v
        self._mods[3] = ProtoBase.TYPE_bytes

    def _mod_end(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        self._mods[3] = ProtoBase.TYPE_bytes

    def _del_end(self):
        self._evermod = True
        if self._pbf_parent_callback:
            self._pbf_parent_callback()
        if 3 in self._cache:
            del self._cache[3]
        if 3 in self._mods:
            del self._mods[3]
        self._buf_del(3)

    _pb_field_name_3 = "end"

    end = property(_get_end, _set_end, _del_end)

    @property
    def end__exists(self):
        return 3 in self._mods or self._buf_exists(3)

    @property
    def end__type(self):
        return ProtoBase.TYPE_bytes

    def _finalize_end(cls):
        if is_string(ProtoBase.TYPE_bytes):
            cls._pbf_strings.append(3)
        elif _PB_type(ProtoBase.TYPE_bytes) is _PB_type:
            assert issubclass(ProtoBase.TYPE_bytes, RepeatedSequence)
            if is_string(ProtoBase.TYPE_bytes.pb_subtype):
                cls._pbf_strings.append(3)

    _pbf_finalizers.append(_finalize_end)


TYPE_AuthTicket = AuthTicket
_PB_finalizers.append('AuthTicket')


for cname in _PB_finalizers:
    eval(cname)._pbf_finalize()

del _PB_finalizers
