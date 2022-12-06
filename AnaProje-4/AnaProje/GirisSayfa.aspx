<%@ Page Title="" Language="C#" MasterPageFile="~/MyMP.Master" AutoEventWireup="true" CodeBehind="GirisSayfa.aspx.cs" Inherits="AnaProje.GirisSayfa" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
     <div>
         <div class="container" >
                <table style="position: absolute top:50% left: 35%" >
                    <tr>
                        <td>
                              <div class="mb-3">
                                <label for="exampleInputEmail1" class="form-label">Email address</label>
                                  <asp:TextBox ID="txtEmail" runat="server"></asp:TextBox>
&nbsp;<div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                              </div>
                        </td>
                     </tr>
                    <tr>
                        <td>
                          <div class="mb-3">
                              Password&nbsp;
                              <asp:TextBox ID="txtPassword" runat="server"></asp:TextBox>
                          </div>
                        </td >
                    </tr>
                    <tr>
                        <td>
                            <div class="mb-3 form-check">
                            <input type="checkbox" class="form-check-input" id="exampleCheck1">
                            <label class="form-check-label" for="exampleCheck1">Check me out</label>
                                <br />
                                <asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
                         </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <asp:Button ID="Button1" runat="server" Text="Giriş" OnClick="Button1_Click" />                  
                            <br />
                            <br />
                            <asp:GridView ID="GridView1" runat="server">
                            </asp:GridView>
                        </td>
                        
                    </tr>
                </table>
         </div>
     </div>
</asp:Content>
