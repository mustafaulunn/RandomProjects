<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="BasvuruFormu.aspx.cs" Inherits="WebApplication3.BasvuruFormu" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Başvuru Formu</title>
    <style type="text/css">
        .auto-style1 {
            width: 255px;
        }
        .auto-style2 {
            width: 255px;
            text-align: right;
        }
        .auto-style3 {
            width: 358px;
        }
        .auto-style4 {
            width: 358px;
            text-align: left;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div>

            <table style="border-color: #808080; border-style: solid; width:100%; background-color: #C0C0C0">
                <tr>
                    <td class="auto-style1" style ="text-align:right">Adi :&nbsp;&nbsp;</td>
                    <td class="auto-style3">
            <asp:TextBox ID="TextBox1" runat="server" OnTextChanged="TextBox1_TextChanged"></asp:TextBox>
                        <asp:RequiredFieldValidator ID="RequiredFieldValidator1" runat="server" ControlToValidate="TextBox1" ErrorMessage="Boş Olmaz" ForeColor="Red"></asp:RequiredFieldValidator>
                    </td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td class="auto-style1" style ="text-align:right">Soyadi:&nbsp; </td>
                    <td class="auto-style3"> <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
                        <asp:RequiredFieldValidator ID="RequiredFieldValidator2" runat="server" ControlToValidate="TextBox2" ErrorMessage="Boş Olmaz" ForeColor="Red"></asp:RequiredFieldValidator>
                    </td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td class="auto-style1" style ="text-align:right">Email: </td>
                    <td class="auto-style3">
                        <asp:TextBox ID="TextBox4" runat="server" TextMode="Email"></asp:TextBox>
                        <asp:RequiredFieldValidator ID="RequiredFieldValidator3" runat="server" ControlToValidate="TextBox4" ErrorMessage="Boş Olmaz" ForeColor="Red"></asp:RequiredFieldValidator>
                    </td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td class="auto-style2">DT: </td>
                    <td class="auto-style3">
            <asp:TextBox ID="TextBox3" runat="server" TextMode="Date"></asp:TextBox>
                        <asp:RequiredFieldValidator ID="RequiredFieldValidator4" runat="server" ControlToValidate="TextBox3" ErrorMessage="Boş Olmaz" ForeColor="Red"></asp:RequiredFieldValidator>
                    </td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td class="auto-style2">Şehir: </td>
                    <td class="auto-style3">
            <asp:DropDownList ID="DropDownList1" runat="server" OnSelectedIndexChanged="DropDownList1_SelectedIndexChanged">
                <asp:ListItem>Adana</asp:ListItem>
                <asp:ListItem>Ankara</asp:ListItem>
                <asp:ListItem>İzmir</asp:ListItem>
                <asp:ListItem>İstanbul</asp:ListItem>
                <asp:ListItem>Bursa</asp:ListItem>
            </asp:DropDownList>
                    </td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td class="auto-style2">Age: </td>
                    <td class="auto-style4">
                        <asp:TextBox ID="TextBox5" runat="server" TextMode="Number"></asp:TextBox>
                        <asp:RequiredFieldValidator ID="RequiredFieldValidator5" runat="server" ControlToValidate="TextBox5" ErrorMessage="Boş Olmaz " ForeColor="Red" Display="Dynamic"></asp:RequiredFieldValidator>
                        <asp:RangeValidator ID="RangeValidator1" runat="server" ControlToValidate="TextBox5" ErrorMessage="18 - 80 arasinda olmasi gerek" ForeColor="Red" MaximumValue="80" MinimumValue="18" Type="Integer" Display="Dynamic"></asp:RangeValidator>
                    </td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td class="auto-style1">&nbsp;</td>
                    <td class="auto-style3">
            <asp:Button ID="Button1" runat="server" Text="Kayit yap" OnClick="Button1_Click" />
                    </td>
                    <td>&nbsp;</td>
                </tr>
                <tr>
                    <td class="auto-style1">&nbsp;</td>
                    <td class="auto-style3">
            <asp:Label ID="Label1" runat="server" Text="merhaba"></asp:Label>
                    </td>
                    <td>&nbsp;</td>
                </tr>
            </table>

        </div>
        <div>
            &nbsp;&nbsp;&nbsp;</div>
    </form>
</body>
</html>
