new Vue({
      el:"#box",
      data() {
        return {
            name: '',
            options: [{
                value: '男',
                label: '男'
        }, {
                value: '女',
                label: '女'
        },],
            options_1: [{
                value: '北京',
                label: '北京'
        }, {
                value: '天津',
                label: '天津'
        }, {
                value: '浙江',
                label: '浙江'
        }, {
                value: '江苏',
                label: '江苏'
        }, {
                value: '山东',
                label: '山东'
        }, {
                value: '广东',
                label: '广东'
        }, {
                value: '广州',
                label: '广州'
        }, {
                value: '上海',
                label: '上海'
        }, {
                value: '四川',
                label: '四川'
        }, {
                value: '其他',
                label: '其他'
        }],
            sex: '',
            address: '',
            phone:'',
            textarea:'',
      }
    },
      methods:{
          handMessageClick() {
              this.$confirm('请确认输入内容正确', '提示', {
                  confirmButtonText: '确认提交',
                  cancelButtonText: '重新填写',
                  type: 'warning',
              })
                  .then(() => {
                      axios({
                          url:'/submit',
                          method:'post',
                          data:{
                              name: this.name,
                              address: this.address,
                              sex:this.sex,
                              phone:this.phone
                          }
                      }).then((res)=> {
                          if (res.data.status === "success") {
                              this.$message({
                                  message:res.data.message,
                                  type:"success"
                              })
                          }else {
                              this.$message({
                                  message:res.data.message,
                                  type:"error"
                              })
                          }
                      })
                  }).catch(() => {
                      this.$message({
                          type: 'info',
                          message: '已取消提交'
                      },
                      )}
                      );
              },
      },
})