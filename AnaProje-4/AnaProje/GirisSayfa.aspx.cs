using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data;
using System.Data.SqlClient;

namespace AnaProje
{
    public partial class GirisSayfa : System.Web.UI.Page
    {
        SqlConnection Baglanti = new SqlConnection();
        SqlCommand Komut = new SqlCommand();
        SqlDataAdapter sqlda = new SqlDataAdapter();
        DataTable dt = new DataTable();
        DataSet ds = new DataSet();

        protected void Page_Load(object sender, EventArgs e)
        {
            Baglanti.ConnectionString = "Data Source=(localdb)\\MSSQLLocalDB;Initial Catalog=MyVT;Integrated Security=True;Connect Timeout=30;";
            Baglanti.Open();
            
        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            ds = new DataSet();
            Komut.CommandText = "SELECT Email, Sifre FROM myTB WHERE Email = '" + txtEmail.Text.ToString() + "' AND Sifre = '"+txtPassword.Text+"'";
            Komut.Connection = Baglanti;
            sqlda = new SqlDataAdapter(Komut);
            sqlda.Fill(ds);
            Komut.ExecuteNonQuery();
            GridView1.DataSource = ds;
            GridView1.DataBind();
            GridView1.Visible = false;

            if(GridView1.Rows.Count > 0)
            {
                Label1.Text = "başarılı";
            }else
            {
                Label1.Text = "başarsız";
            }
            Baglanti.Close();



        }

        
    }
}