<?php
/* Smarty version 3.1.48, created on 2023-11-14 17:36:07
  from '/var/www/html/modules/paypal/views/templates/admin/_partials/featureChecklist.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_6553a1f7e747c8_73949865',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'e2a41d99bdd857f105dcf3f3481f39e097f29195' => 
    array (
      0 => '/var/www/html/modules/paypal/views/templates/admin/_partials/featureChecklist.tpl',
      1 => 1699618312,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6553a1f7e747c8_73949865 (Smarty_Internal_Template $_smarty_tpl) {
?><div class="row pb-3 h-100">
  <div class="col-12 col-lg-9 col-xl-8 pb-4">
    <ul class="list-unstyled mb-0">
      <?php if ((isset($_smarty_tpl->tpl_vars['vars']->value['isBnplEnabled']))) {?>
        <li class="d-flex align-items-center mb-1">
          <?php $_smarty_tpl->_subTemplateRender(($_smarty_tpl->tpl_vars['moduleFullDir']->value).("/views/templates/admin/_partials/icon-status.tpl"), $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array('isSuccess'=>(($tmp = @$_smarty_tpl->tpl_vars['vars']->value['isBnplEnabled'])===null||$tmp==='' ? false : $tmp)), 0, true);
?>
          <?php if ($_smarty_tpl->tpl_vars['vars']->value['isBnplEnabled']) {?>
            <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Buy now pay later enabled','mod'=>'paypal'),$_smarty_tpl ) );?>

          <?php } else { ?>
            <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Buy now pay later disabled','mod'=>'paypal'),$_smarty_tpl ) );?>

          <?php }?>
        </li>
      <?php }?>

      <?php if ((($tmp = @$_smarty_tpl->tpl_vars['vars']->value['isShortcutCustomized'])===null||$tmp==='' ? false : $tmp)) {?>
        <li class="d-flex align-items-center mb-1">
            <?php $_smarty_tpl->_subTemplateRender(($_smarty_tpl->tpl_vars['moduleFullDir']->value).("/views/templates/admin/_partials/icon-status.tpl"), $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array('isSuccess'=>true), 0, true);
?>
            <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Customized shortcut button enabled','mod'=>'paypal'),$_smarty_tpl ) );?>

        </li>
      <?php }?>

      <?php if ((isset($_smarty_tpl->tpl_vars['vars']->value['isCreditCardEnabled']))) {?>
        <li class="d-flex align-items-center mb-1">
            <?php $_smarty_tpl->_subTemplateRender(($_smarty_tpl->tpl_vars['moduleFullDir']->value).("/views/templates/admin/_partials/icon-status.tpl"), $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array('isSuccess'=>$_smarty_tpl->tpl_vars['vars']->value['isCreditCardEnabled']), 0, true);
?>

            <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Credit card enabled','mod'=>'paypal'),$_smarty_tpl ) );?>

        </li>
      <?php }?>

      <?php if ((isset($_smarty_tpl->tpl_vars['vars']->value['isPuiEnabled']))) {?>
        <li class="d-flex align-items-center mb-1">
          <?php $_smarty_tpl->_subTemplateRender(($_smarty_tpl->tpl_vars['moduleFullDir']->value).("/views/templates/admin/_partials/icon-status.tpl"), $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array('isSuccess'=>(($tmp = @$_smarty_tpl->tpl_vars['vars']->value['isPuiEnabled'])===null||$tmp==='' ? false : $tmp)), 0, true);
?>
          <?php if ($_smarty_tpl->tpl_vars['vars']->value['isPuiEnabled']) {?>
            <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'PUI enabled','mod'=>'paypal'),$_smarty_tpl ) );?>

          <?php } else { ?>
            <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'PUI disabled','mod'=>'paypal'),$_smarty_tpl ) );?>

          <?php }?>
        </li>
      <?php }?>

      <li class="d-flex align-items-center mb-1">
        <?php $_smarty_tpl->_subTemplateRender(($_smarty_tpl->tpl_vars['moduleFullDir']->value).("/views/templates/admin/_partials/icon-status.tpl"), $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array('isSuccess'=>true), 0, true);
?>
        <?php if ((($tmp = @$_smarty_tpl->tpl_vars['vars']->value['isOrderStatusCustomized'])===null||$tmp==='' ? false : $tmp)) {?>
          <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Customized order status enabled','mod'=>'paypal'),$_smarty_tpl ) );?>

        <?php } else { ?>
          <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Standard order status','mod'=>'paypal'),$_smarty_tpl ) );?>

        <?php }?>
      </li>

      <li class="d-flex align-items-center">
        <?php $_smarty_tpl->_subTemplateRender(($_smarty_tpl->tpl_vars['moduleFullDir']->value).("/views/templates/admin/_partials/icon-status.tpl"), $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array('isSuccess'=>(($tmp = @$_smarty_tpl->tpl_vars['vars']->value['isShowPaypalBenefits'])===null||$tmp==='' ? false : $tmp)), 0, true);
?>
          <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'PayPal benefits enabled','mod'=>'paypal'),$_smarty_tpl ) );?>

      </li>

      <li class="d-flex align-items-center">
          <?php $_smarty_tpl->_subTemplateRender(($_smarty_tpl->tpl_vars['moduleFullDir']->value).("/views/templates/admin/_partials/icon-status.tpl"), $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array('isSuccess'=>true), 0, true);
?>
          <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Tracking enabled','mod'=>'paypal'),$_smarty_tpl ) );?>

      </li>
    </ul>
  </div>

  <div class="col-12 col-lg-3 col-xl-4 align-items-end d-flex justify-content-end">
    <button class="btn btn-secondary ml-auto" refresh-feature-checklist><?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Refresh','mod'=>'paypal'),$_smarty_tpl ) );?>
</button>
  </div>

</div>
<?php }
}
