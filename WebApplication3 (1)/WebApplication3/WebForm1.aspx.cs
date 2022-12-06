using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication3
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void CheckBox1_CheckedChanged(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            if(TextBox1.Text == "Ali" && TextBox2.Text == "123")
            {
                Response.Redirect("BasvuruFormu.aspx");
            }
            else
            {
                Label1.Text = "Kulanci adi veya Şifre yanlış";
            }
        }
    }
}