<?php
/* Smarty version 3.1.48, created on 2023-11-14 17:36:07
  from '/var/www/html/modules/paypal/views/templates/admin/_partials/messages/form-help-info/account.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_6553a1f7e009f2_61216744',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '7e56c358e43287583dc767892c501e4e823a9757' => 
    array (
      0 => '/var/www/html/modules/paypal/views/templates/admin/_partials/messages/form-help-info/account.tpl',
      1 => 1699618312,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6553a1f7e009f2_61216744 (Smarty_Internal_Template $_smarty_tpl) {
?>
<div class="h4">
  <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'How can I log in with my PayPal account ?','mod'=>'paypal'),$_smarty_tpl ) );?>

</div>
<br>
<p>
  <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Before connecting your shop with your PayPal account, please select the mode of connection. There is 2 connection modes :','mod'=>'paypal'),$_smarty_tpl ) );?>

</p>

<p>
  <?php ob_start();
echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'[b]Sandbox[/b] mode allows you a mock link to test the flow between Prestashop and PayPal. You can test as long as needed. If you want to create an account, please use the button "Connect or create your PayPal account".','mod'=>'paypal'),$_smarty_tpl ) );
$_prefixVariable8 = ob_get_clean();
echo smarty_modifier_paypalreplace($_prefixVariable8,array());?>

</p>
<p>
    <?php ob_start();
echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'[b]Production[/b] mode allows you to sell our products online and be paid by customers. If you want to create an account, please click use the button "Connect or create your PayPal account".','mod'=>'paypal'),$_smarty_tpl ) );
$_prefixVariable9 = ob_get_clean();
echo smarty_modifier_paypalreplace($_prefixVariable9,array());?>

</p>
<p>
  <?php ob_start();
echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'[b]Note:[/b] You need to switch to the “Production” mode to activate your payment solution.','mod'=>'paypal'),$_smarty_tpl ) );
$_prefixVariable10 = ob_get_clean();
echo smarty_modifier_paypalreplace($_prefixVariable10,array());?>

</p>
<?php }
}
