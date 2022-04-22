/**
 * 为空校验
 * @param {*} s
 */
export function isBlank (s) {
  return /\S/.test(s)
}

/**
 * 邮箱
 * @param {*} s
 */
export function isEmail (s) {
  return /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((.[a-zA-Z0-9_-]{2,3}){1,2})$/.test(s)
}

/**
 * 手机号码
 * @param {*} s
 */
export function isMobile (s) {
  return /^1[0-9]{10}$/.test(s)
}

/**
 * 电话号码
 * @param {*} s
 */
export function isPhone (s) {
  return /^([0-9]{3,4}-)?[0-9]{7,8}$/.test(s)
}
/**
 * 身份证
 * @param {*} s
 */
export function cardID (s) {
  // 15位和18位身份证号码的正则表达式
  return /^(^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$)|(^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])((\d{4})|\d{3}[Xx])$)$/.test(s)
}
/**
 * 数字验证
 * @param {*} s
 */
export function numberTwo (s) {
  // 15位和18位身份证号码的正则表达式
  return /\b\d{1,2}\b/g.test(s)
}
/**
 * 密码校验
 * @param {*} s
 * 密码不能少于6位，最大30位，且包含字母、数字
 */
export function pwdFormat (s) {
  /**
   * (?=.*[0-9] )     数字
   * (?=.*[a-zA-Z])   字母
   * {6,30}           6-30位
   */
  // let regex = new RegExp(/(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[^a-zA-Z0-9]).{6,30}/)
  // let regex = /^(?![a-zA-Z]+$)(?![A-Z0-9]+$)(?![A-Z\\W_]+$)(?![a-z0-9]+$)(?![a-z\\W_]+$)(?![0-9\\\\W_]+$)[a-zA-Z0-9\\W_]{6,}$/
  // return regex.test(s)
  if (s == null || s.length < 6) return false
  let reg = new RegExp(/^(?![^a-zA-Z]+$)(?!\D+$)/)
  return !!reg.test(s)
}
/**
 * URL地址
 * @param {*} s
 */
export function isURL (s) {
  return /^http[s]?:\/\/.*/.test(s)
}
/**
 * 时间格式化
 * @param {*}
 */
// eslint-disable-next-line no-extend-native
Date.prototype.Format = function (fmt) {
  var o = {
    'M+': this.getMonth() + 1, // 月份
    'd+': this.getDate(), // 日
    'h+': this.getHours(), // 小时
    'm+': this.getMinutes(), // 分
    's+': this.getSeconds(), // 秒
    'q+': Math.floor((this.getMonth() + 3) / 3), // 季度
    'S': this.getMilliseconds() // 毫秒
  }
  if (/(y+)/.test(fmt)) {
    fmt = fmt.replace(RegExp.$1, (this.getFullYear() + '').substr(4 - RegExp.$1.length))
  }
  for (var k in o) {
    if (new RegExp('(' + k + ')').test(fmt)) {
      fmt = fmt.replace(RegExp.$1, (RegExp.$1.length === 1) ? (o[k]) : (('00' + o[k]).substr(('' + o[k]).length)))
    }
  }
  return fmt
}

/**
 * 系统校验
 * @param {*} s
 */
export function isSystemVersion (s) {
  let version = navigator.userAgent.toLowerCase()
  let mac = version.indexOf('mac')
  let os = version.indexOf('os')
  let bool = false
  if (mac > 0 && os > 0) {
    // 苹果系统下执行的操作
    bool = s === 'mac'
  } else {
    // windows系统下执行的操作
    bool = s === 'windows'
  }
  return bool
}

/**
 * 浏览器校验
 * @param {*} s
 */
export function isBrowserVersion (s) {
  let userAgent = navigator.userAgent // 取得浏览器的userAgent字符串
  let isOpera = userAgent.indexOf('Opera') > -1
  let bool = false
  if (isOpera) {
    bool = s === 'Opera'
  }
  // 判断是否Opera浏览器
  if (userAgent.indexOf('Firefox') > -1) {
    bool = s === 'FF'
  } // 判断是否Firefox浏览器
  if (userAgent.indexOf('Chrome') > -1) {
    bool = s === 'Chrome'
  }
  if (userAgent.indexOf('Safari') > -1) {
    bool = s === 'Safari'
  } // 判断是否Safari浏览器
  if (userAgent.indexOf('compatible') > -1 && userAgent.indexOf('MSIE') > -1 && !isOpera) {
    bool = s === 'IE'
  } // 判断是否IE浏览器
  return bool
}

/**
 * 校验两个对象是否相同
 * @param {} obj1, obj2
 */
export function diff (x, y) {
  if (x === y) {
    return true
  }
  if (!(x instanceof Object) || !(y instanceof Object)) {
    return false
  }
  if (x.constructor !== y.constructor) {
    return false
  }
  for (var p in x) {
    if (x.hasOwnProperty(p)) {
      if (!y.hasOwnProperty(p)) {
        return false
      }
      if (x[p] === y[p]) {
        continue
      }
      if (typeof (x[p]) !== 'object') {
        return false
      }
      if (!Object.equals(x[p], y[p])) {
        return false
      }
    }
  }
  for (p in y) {
    if (y.hasOwnProperty(p) && !x.hasOwnProperty(p)) {
      return false
    }
  }
  return true
}
