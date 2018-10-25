/*
A KBase module: ProteinStructureUtils
*/

module ProteinStructureUtils {
    /* A boolean - 0 for false, 1 for true.
    @range (0, 1)
  */
  typedef int boolean;

  /* An X/Y/Z style reference
    @id ws
  */
  typedef string obj_ref;

  /* workspace name of the object */
  typedef string workspace_name;

  typedef structure {
      obj_ref input_ref;
      string destination_dir;
   } StructureToPDBFileParams;

  typedef structure {
      string file_path;
  } StructureToPDBFileOutput;

  funcdef structure_to_pdb_file(StructureToPDBFileParams params)
      returns (StructureToPDBFileOutput result) authentication required;

  /* Input of the export_pdb function
    obj_ref: generics object reference
  */
  typedef structure {
      obj_ref obj_ref;
  } ExportParams;

  typedef structure {
      string shock_id;
  } ExportOutput;

  funcdef export_pdb (ExportParams params) returns (ExportOutput result) authentication required;

  /* Input of the import_matrix_from_excel function
    input_shock_id: file shock id
    input_file_path: absolute file path
    input_staging_file_path: staging area file path
    structure_name: structure object name
    workspace_name: workspace name for object to be saved to

  */
  typedef structure {
      string input_shock_id;
      string input_file_path;
      string input_staging_file_path;
      string structure_name;
      string description;
      workspace_name workspace_name;
  } ImportPDBParams;

  typedef structure {
      string report_name;
      string report_ref;
      obj_ref structure_obj_ref;
  } ImportPDBOutput;

  /* import_pdb_from_staging: import a ProteinStructure from PDB*/
  funcdef import_pdb_file (ImportPDBParams params) returns (ImportPDBOutput result) authentication required;

};
