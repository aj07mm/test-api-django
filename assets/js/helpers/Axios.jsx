const Axios = require('axios');

const axiosInstance = Axios.create({
  xsrfCookieName: 'twyla-csrftoken-2',
  xsrfHeaderName: 'X-CSRFToken',
  headers: { 'X-Requested-With': 'XMLHttpRequest' },
});

export default { ...Axios, ...axiosInstance };
